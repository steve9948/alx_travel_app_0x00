# Summary of How to Use

## 1. Set Up the Project
- Create a Django project and an app called `listings`.

## 2. Define Models
- Create `Listing`, `Booking`, and `Review` models with the necessary relationships between them.

## 3. Create Serializers
- Serialize the data using Django REST Framework by creating serializers for `Listing` and `Booking` models.

## 4. Create Seeder Command
- Use a custom management command to populate the database with sample data (e.g., create a set number of listings, bookings, and reviews).

## 5. Run the App
- Start the Django development server.
- Use the seed command (`python manage.py seed <num>`) to populate the database with sample data.

## 6. Expand
- Add additional features such as authentication, API views, and integrate with real data sources for a complete application.

---

With these steps, you can easily set up the core functionality of your Django project, allowing you to handle listings, bookings, and reviews with sample data.
