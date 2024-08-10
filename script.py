from webscrape import download_images

fruits = ['banana', 'strawberry', 'apple', 'grape', 'melon', 'avocado', 'orange', 'peach', 'pineapple', 'mango']
vegetables = ['potatoe', 'onion', 'tomatoe', 'lettuce', 'carrot', 'pepper', 'cucumber', 'celery', 'brocolli']

for fruit in fruits:
    diseased = "diseased " + fruit + " trees"
    healthy = "healthy " + fruit + " trees"

    diseased_folder = "diseased " + fruit
    healthy_folder = "healthy " + fruit

    download_images(diseased, 100, diseased_folder)
    download_images(healthy, 100, healthy_folder)

for vegetable in vegetables:
    diseased = "diseased " + vegetable + " trees"
    healthy = "healthy " + vegetable + " trees"

    diseased_folder = "diseased " + vegetable
    healthy_folder = "healthy " + vegetable

    download_images(diseased, 100, diseased_folder)
    download_images(healthy, 100, healthy_folder)
