.PHONY: task00 task01 task0203

task00:
		cd task00 && sudo docker build -t my-python-app . && sudo docker run -it my-python-app
task01:
		cd task01 && sudo docker build -t my-flask-app . && sudo docker run -p 5000:5000 my-flask-app
task0203:
		cd task02 && sudo docker build -t tf-flowers-model . && docker run -it tf-flowers-model