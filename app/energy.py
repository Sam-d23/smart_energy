import pandas as pd
import matplotlib.pyplot as plt
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import EnergyData, db
from datetime import datetime, timedelta


bp = Blueprint('energy', __name__)


@bp.route('/dashboard')
@login_required
def dashboard():
    generate_energy_data()
    plot_path = plot_energy_usage()
    return render_template('dashboard.html', plot_path=plot_path)

def generate_energy_data():
    # Generate energy data for the last week
    for i in range(7 * 24):  # 7 days, hourly data
        data = EnergyData(
            usage=round(0.5 + i * 0.02, 2),  # Example: increasing usage
            temperature=round(20 + i * 0.05, 2),
            humidity=round(50 + i * 0.03, 2),
            user_id=current_user.id
        )
        db.session.add(data)
    db.session.commit()

def plot_energy_usage():
    data = EnergyData.query.filter_by(user_id=current_user.id).all()
    if not data:
        return None
    
    timestamps = [d.timestamp for d in data]
    usage = [d.usage for d in data]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, usage, marker='o')
    plt.title('Energy Usage Over the Last Week')
    plt.xlabel('Time')
    plt.ylabel('Usage (kWh)')
    plt.grid(True)

    plot_path = 'app/static/plots/energy_usage.png'
    plt.savefig(plot_path)
    return plot_path
