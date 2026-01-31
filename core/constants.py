from decouple import config

DEV = "DEV"
PROD = "PROD"
BRAND_NAME = config("BRAND_NAME", default="Core")
VERSION = config("VERSION", default="1.0.0")
