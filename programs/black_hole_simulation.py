import numpy as np
import matplotlib.pyplot as plt

# Constants
PI = np.pi

def checkerAA(p):
    # Create a checkerboard pattern using sine functions
    q = np.sin(PI * p * np.array([20, 10]))
    m = q[0] * q[1]
    return 0.5 - m

def raytrace_blackhole(resolution, hfov, dist, iTime, max_iterations=100):
    width, height = resolution
    img = np.zeros((height, width, 3))  # Initialize image with zeros

    for y in range(height):
        for x in range(width):
            # Normalized coordinates (uv)
            uv = (2.0 * np.array([x, y]) - np.array([width, height])) / width

            # Calculate the ray direction
            vel = np.array([1.0, -uv[0] * np.tan(hfov / 2), -uv[1] * np.tan(hfov / 2)])
            vel /= np.linalg.norm(vel)  # Normalize the velocity vector

            # Initialize position and radius
            pos = np.array([-dist, 0., 0.])
            r = np.linalg.norm(pos)
            dtau = 0.2

            # Ray-tracing loop with a limit on iterations
            for iterations in range(max_iterations):
                ddtau = dtau * r
                pos += vel * ddtau
                r = np.linalg.norm(pos)

                # Break if the ray is too close to the singularity
                if r <= 0.1:
                    break

                er = pos / r
                c = np.cross(vel, er)
                vel -= ddtau * np.dot(c, c) * er / (r ** 2)

            # Calculate spherical coordinates for texture mapping if ray escaped
            if r > 1.0:
                phi1 = 1.0 - np.arctan2(vel[1], vel[0]) / (2.0 * PI)
                theta1 = 1.0 - np.arctan2(np.linalg.norm(vel[:2]), vel[2]) / PI
                UV = np.array([phi1, theta1]) + np.array([iTime * 0.01, 0.0])

                # Checker pattern color
                rgb = np.array([checkerAA(UV * 180.0 / PI / 30.0)])
                img[y, x] = rgb  # Store the RGB color in the image array

    return img

# Main settings
resolution = (400, 200)  # width, height
hfov = 2.3  # Horizontal field of view
dist = 3.0  # Distance from the black hole
iTime = 0.0  # Time, used for animation (if needed)

# Generate the black hole image
image = raytrace_blackhole(resolution, hfov, dist, iTime)

# Display the image using matplotlib
plt.imshow(image, extent=[-1, 1, -0.5, 0.5])
plt.title("Black Hole Distortion")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("off")  # Turn off the axis for better visualization
plt.show()
