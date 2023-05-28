from flask import Flask, render_template, request

app = Flask(__name__)

class Car:
    def __init__(self, make, model, price, image_url):
        self.make = make
        self.model = model
        self.price = price
        self.image_url = image_url

class CarSuggestionSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, make, model, price, image_url):
        car = Car(make, model, price, image_url)
        self.cars.append(car)

    def suggest_cars(self, date, preferred_model):
        suggested_cars = []
        for car in self.cars:
            if car.model.lower() == preferred_model.lower():
                suggested_cars.append(car)
        return suggested_cars

suggestion_system = CarSuggestionSystem()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggestions', methods=['POST'])
def get_suggestions():
    date = request.form['date']
    preferred_model = request.form['preferred_model']
    suggested_cars = suggestion_system.suggest_cars(date, preferred_model)
    return render_template('suggestions.html', cars=suggested_cars)

if __name__ == '__main__':
    # Add cars to the system
    suggestion_system.add_car("Toyota", "Corolla", 15000, "https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cms.haymarketindia.net/model/uploads/modelimages/BMW-2-Series-Gran-Coupe-271220221147.jpg&w=373&h=245&q=75&c=1")
    suggestion_system.add_car("Toyota", "Corolla", 16000, "https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cms.haymarketindia.net/model/uploads/modelimages/BMW-2-Series-Gran-Coupe-271220221147.jpg&w=373&h=245&q=75&c=1")
    suggestion_system.add_car("Toyota", "Corolla", 17000, "https://cdni.autocarindia.com/Utils/ImageResizer.ashx?n=https://cms.haymarketindia.net/model/uploads/modelimages/BMW-2-Series-Gran-Coupe-271220221147.jpg&w=373&h=245&q=75&c=1")
    suggestion_system.add_car("Honda", "Civic", 18000, "https://example.com/honda_civic_1.jpg")
    suggestion_system.add_car("Honda", "Civic", 19000, "https://example.com/honda_civic_2.jpg")
    suggestion_system.add_car("Honda", "Civic", 20000, "https://example.com/honda_civic_3.jpg")
    suggestion_system.add_car("Ford", "Mustang", 35000, "https://example.com/ford_mustang_1.jpg")
    suggestion_system.add_car("Ford", "Mustang", 36000, "https://example.com/ford_mustang_2.jpg")
    suggestion_system.add_car("Ford", "Mustang", 37000, "https://example.com/ford_mustang_3.jpg")
    suggestion_system.add_car("Chevrolet", "Camaro", 40000, "https://example.com/chevrolet_camaro_1.jpg")
    suggestion_system.add_car("Chevrolet", "Camaro", 41000, "https://example.com/chevrolet_camaro_2.jpg")
    suggestion_system.add_car("Chevrolet", "Camaro", 42000, "https://example.com/chevrolet_camaro_3.jpg")

    app.run(debug=True)
