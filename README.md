# MNIST classification by TensorFlow #

- [MNIST For ML Beginners](https://www.tensorflow.org/tutorials/mnist/beginners/)
- [Deep MNIST for Experts](https://www.tensorflow.org/tutorials/mnist/pros/)

![screencast](https://cloud.githubusercontent.com/assets/80381/11339453/f04f885e-923c-11e5-8845-33c16978c54d.gif)

### Requirement ###

- Python >=3.4
  - TensorFlow 0.11.0
- Node >=6.9


### How to run ###

    $ pip install -r requirements.txt
    $ npm install
    $ gunicorn main:app --reload --bind=192.168.1.7:8000

    Or run classifier process only:

    $ python ./inception/classify_image.py  --model_dir=/home/frateant/codebase/ftraian/deep-learning/inception_v3


### Deploy to Heroku ###

    $ heroku apps:create [NAME]
    $ heroku buildpacks:add heroku/nodejs
    $ heroku buildpacks:add heroku/python
    $ git push heroku master

or Heroku Button.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
