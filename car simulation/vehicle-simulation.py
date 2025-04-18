import tkinter as tk
import random
from math import sin, cos, pi

class VehicleSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Simulation")
        self.root.geometry("800x600")
        
        # Canvas for drawing
        self.canvas = tk.Canvas(root, width=800, height=500, bg="light blue")
        self.canvas.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Create buttons for each vehicle
        self.car_button = tk.Button(button_frame, text="Show BMW Car", command=self.draw_car)
        self.car_button.grid(row=0, column=0, padx=10)
        
        self.truck_button = tk.Button(button_frame, text="Show Toyota Truck", command=self.draw_truck)
        self.truck_button.grid(row=0, column=1, padx=10)
        
        self.suv_button = tk.Button(button_frame, text="Show Volvo SUV", command=self.draw_suv)
        self.suv_button.grid(row=0, column=2, padx=10)
        
        # Flower positions
        self.flower_positions = [
            (100, 450), (200, 470), (300, 460), 
            (500, 470), (600, 450), (700, 460)
        ]
        
        # Initial flower color
        self.flower_color = self.random_color()
        
        # Draw initial flowers
        self.draw_flowers()
    
    def draw_flowers(self):
        """Draw 6 flowers with the same random color"""
        self.canvas.delete("flower")
        
        # Generate a single color for all flowers
        self.flower_color = self.random_color()
        center_color = self.random_color()
        
        for x, y in self.flower_positions:
            self.draw_flower(x, y, self.flower_color, center_color)
    
    def draw_flower(self, x, y, petal_color, center_color):
        """Draw a flower at the specified position with given colors"""
        stem_color = "green"
        
        # Draw stem
        self.canvas.create_line(x, y, x, y+50, width=4, fill=stem_color, tags="flower")
        
        # Draw petals
        petal_size = 15
        for i in range(8):
            angle = i * pi/4
            x1 = x + petal_size * cos(angle)
            y1 = y + petal_size * sin(angle)
            self.canvas.create_oval(
                x1-petal_size, y1-petal_size, 
                x1+petal_size, y1+petal_size, 
                fill=petal_color, outline="", tags="flower"
            )
        
        # Draw center
        self.canvas.create_oval(
            x-10, y-10, x+10, y+10, 
            fill=center_color, outline="black", tags="flower"
        )
    
    def random_color(self):
        """Generate a random color in hex format"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def clear_vehicles(self):
        """Clear all vehicles from the canvas"""
        self.canvas.delete("vehicle")
    
    def draw_car(self):
        """Draw a BMW car with random size and color"""
        self.clear_vehicles()
        # Update flowers with new color
        self.draw_flowers()
        
        # Random car properties
        car_color = self.random_color()
        size_factor = random.uniform(0.8, 1.2)
        
        # Base position
        x, y = 400, 300
        
        # Car body dimensions
        width = int(180 * size_factor)
        height = int(40 * size_factor)
        
        # Draw car body
        self.canvas.create_rectangle(
            x - width/2, y - height/2, 
            x + width/2, y - height*2, 
            fill=car_color, outline="black", width=2, tags="vehicle"
        )
        
        # Draw car top
        self.canvas.create_polygon(
            x - width/3, y - height*2,
            x - width/6, y - height*3,
            x + width/6, y - height*3,
            x + width/3, y - height*2,
            fill=car_color, outline="black", width=2, tags="vehicle"
        )
        
        # Draw windows
        window_color = "light blue"
        # Left window
        self.canvas.create_rectangle(
            x - width/3 + 5, y - height*2 + 5,
            x - width/6 + 5, y - height*3 + 5,
            fill=window_color, outline="black", tags="vehicle"
        )
        # Right window
        self.canvas.create_rectangle(
            x + width/6 - 5, y - height*2 + 5,
            x - width/6 + 5, y - height*3 + 5,
            fill=window_color, outline="black", tags="vehicle"
        )
        
        # Draw wheels
        wheel_radius = int(20 * size_factor)
        # Left wheel
        self.canvas.create_oval(
            x - width/3 - wheel_radius, y - wheel_radius,
            x - width/3 + wheel_radius, y + wheel_radius,
            fill="black", tags="vehicle"
        )
        # Right wheel
        self.canvas.create_oval(
            x + width/3 - wheel_radius, y - wheel_radius,
            x + width/3 + wheel_radius, y + wheel_radius,
            fill="black", tags="vehicle"
        )
        
        # Draw BMW logo
        self.canvas.create_oval(
            x - 10, y - height*2 - 10,
            x + 10, y - height*2 + 10,
            fill="white", outline="black", tags="vehicle"
        )
        self.canvas.create_text(
            x, y - height*2,
            text="BMW", font=("Arial", 8), tags="vehicle"
        )
    
    def draw_truck(self):
        """Draw a Toyota truck with random size and color"""
        self.clear_vehicles()
        # Update flowers with new color
        self.draw_flowers()
        
        # Random truck properties
        truck_color = self.random_color()
        size_factor = random.uniform(0.8, 1.2)
        
        # Base position
        x, y = 400, 300
        
        # Truck dimensions
        width = int(200 * size_factor)
        height = int(50 * size_factor)
        
        # Draw truck cab
        cab_width = width / 3
        self.canvas.create_rectangle(
            x - width/2, y - height/2,
            x - width/2 + cab_width, y - height*2,
            fill=truck_color, outline="black", width=2, tags="vehicle"
        )
        
        # Draw truck bed
        self.canvas.create_rectangle(
            x - width/2 + cab_width, y - height/2,
            x + width/2, y - height,
            fill=truck_color, outline="black", width=2, tags="vehicle"
        )
        
        # Draw windows
        window_color = "light blue"
        self.canvas.create_rectangle(
            x - width/2 + 5, y - height*2 + 5,
            x - width/2 + cab_width - 5, y - height - 5,
            fill=window_color, outline="black", tags="vehicle"
        )
        
        # Draw wheels
        wheel_radius = int(25 * size_factor)
        # Front wheel
        self.canvas.create_oval(
            x - width/3 - wheel_radius, y - wheel_radius,
            x - width/3 + wheel_radius, y + wheel_radius,
            fill="black", tags="vehicle"
        )
        # Back wheel
        self.canvas.create_oval(
            x + width/4 - wheel_radius, y - wheel_radius,
            x + width/4 + wheel_radius, y + wheel_radius,
            fill="black", tags="vehicle"
        )
        
        # Draw Toyota logo
        self.canvas.create_oval(
            x - width/2 + cab_width/2 - 15, y - height*1.5 - 10,
            x - width/2 + cab_width/2 + 15, y - height*1.5 + 10,
            fill="red", outline="black", tags="vehicle"
        )
        self.canvas.create_text(
            x - width/2 + cab_width/2, y - height*1.5,
            text="TOYOTA", font=("Arial", 8), fill="white", tags="vehicle"
        )
        
        # Draw 4WD label
        self.canvas.create_text(
            x, y - height/2 - 10,
            text="4WD", font=("Arial", 12, "bold"), tags="vehicle"
        )
    
    def draw_suv(self):
        """Draw a Volvo SUV with random size and color"""
        self.clear_vehicles()
        # Update flowers with new color
        self.draw_flowers()
        
        # Random SUV properties
        suv_color = self.random_color()
        size_factor = random.uniform(0.8, 1.2)
        
        # Base position
        x, y = 400, 300
        
        # SUV dimensions
        width = int(220 * size_factor)
        height = int(60 * size_factor)
        
        # Draw SUV body
        self.canvas.create_rectangle(
            x - width/2, y - height/2,
            x + width/2, y - height*2,
            fill=suv_color, outline="black", width=2, tags="vehicle"
        )
        
        # Draw SUV roof
        self.canvas.create_rectangle(
            x - width/2 + width/8, y - height*2,
            x + width/2 - width/8, y - height*2.7,
            fill=suv_color, outline="black", width=2, tags="vehicle"
        )
        
        # Draw windows
        window_color = "light blue"
        # Front window
        self.canvas.create_rectangle(
            x - width/3, y - height*2 + 5,
            x - width/8, y - height*2.65,
            fill=window_color, outline="black", tags="vehicle"
        )
        # Middle window
        self.canvas.create_rectangle(
            x - width/8 + 5, y - height*2 + 5,
            x + width/8 - 5, y - height*2.65,
            fill=window_color, outline="black", tags="vehicle"
        )
        # Back window
        self.canvas.create_rectangle(
            x + width/8, y - height*2 + 5,
            x + width/3, y - height*2.65,
            fill=window_color, outline="black", tags="vehicle"
        )
        
        # Draw wheels
        wheel_radius = int(30 * size_factor)
        # Front wheel
        self.canvas.create_oval(
            x - width/3 - wheel_radius, y - wheel_radius,
            x - width/3 + wheel_radius, y + wheel_radius,
            fill="black", tags="vehicle"
        )
        # Back wheel
        self.canvas.create_oval(
            x + width/3 - wheel_radius, y - wheel_radius,
            x + width/3 + wheel_radius, y + wheel_radius,
            fill="black", tags="vehicle"
        )
        
        # Draw Volvo logo
        self.canvas.create_oval(
            x - 15, y - height*1.5 - 10,
            x + 15, y - height*1.5 + 10,
            fill="silver", outline="black", tags="vehicle"
        )
        self.canvas.create_text(
            x, y - height*1.5,
            text="VOLVO", font=("Arial", 8), tags="vehicle"
        )
        
        # Draw passenger capacity
        self.canvas.create_text(
            x, y - height/2 - 10,
            text="5 Passengers", font=("Arial", 12, "bold"), tags="vehicle"
        )

def main():
    root = tk.Tk()
    app = VehicleSimulation(root)
    root.mainloop()

if __name__ == "__main__":
    main()