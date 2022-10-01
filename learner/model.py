import os
import timm
from fastai.vision.widgets import *
from fastai.vision.all import *
from duckduckgo_search import ddg_images

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "categories")


def download_image_set():
    product_categories = "baby products", "beauty products", "camera and photo products", "mobile phone", "clothes", "consumer electronics products", "fine art", "health and personal care products", "garden products", "home tools", "major appliances", "musical instruments products", "office supplies products", "pet supplies products", "sports products", "toys and games", "watches", "mobile phone accessories"

    for category in product_categories:
        dest = os.path.join(path, category)
        os.makedirs(dest, exist_ok=True)
        results = ddg_images(category, safesearch="Off", max_results=300)
        imageUrls = []
        for result in results:
            imageUrls.append(result["image"])
        download_images(dest, urls=imageUrls)

    fns = get_image_files(path)

    failed = verify_images(fns)

    failed.map(Path.unlink)


def export_model():
    try:
        # only for machine withput GPU
        os.environ["OMP_NUM_THREADS"] = "1"

        if not os.path.isdir(path):
            download_image_set()

        categories = DataBlock(
            blocks=(ImageBlock, CategoryBlock),
            get_items=get_image_files,
            splitter=RandomSplitter(valid_pct=0.2, seed=42),
            get_y=parent_label,
            item_tfms=RandomResizedCrop(224, min_scale=0.5),
            batch_tfms=aug_transforms()
        )

        dls = categories.dataloaders(path)

        learn = vision_learner(
            dls, 'convnext_base_in22ft1k', metrics=error_rate)

        learn.fine_tune(4)

        learn.export(fname="model/product-categories.pkl")
    except Exception as e:
        return e
