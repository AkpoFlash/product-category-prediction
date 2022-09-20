from fastai.vision.all import *

inferencer = load_learner("model/product-categories.pkl")

image_categories = inferencer.dls.vocab


def classify_image(img):
    pred, idx, probs = inferencer.predict(img)
    return dict(zip(image_categories, map(float, probs)))
