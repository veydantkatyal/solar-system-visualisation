import numpy as np
import plotly.graph_objects as go

def create_sphere(radius, distance, color):
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    x = distance + (radius * np.sin(phi) * np.cos(theta))
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return go.Surface(x=x, y=y, z=z, colorscale=[[0, color], [1, color]], showscale=False)

def create_orbit(radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = np.zeros_like(theta)

    return go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='white', width=2))
