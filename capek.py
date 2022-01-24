from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None


class Home(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "top": [
                                {
                                    "left": [
                                        {
                                            "icon": "envelop",
                                            "text": "hello@colorlib.com"
                                        },
                                        {
                                            "text": "Free Shipping for all Order of $99"
                                        }
                                    ]
                                },
                                {
                                    "right": [
                                        {
                                            "sosmed": [
                                                {
                                                    "icon": "facebook",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "icon": "linkedin",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "icon": "pinterest",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                }
                                            ]
                                        },
                                        {
                                            "language": [
                                                {
                                                    "image": "data:image/webp;base64,UklGRowAAABXRUJQVlA4IIAAAAB…mY93zrj0P0ea+n9DmVodGk7RubcK/qHhB4yLFEzBhQuGAAA==",
                                                    "text": "English",
                                                    "availablelanguage": [
                                                        {
                                                            "text": "Spanis",
                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                        },
                                                        {
                                                            "text": "English",
                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "login": {
                                                "icon": "user",
                                                "text": "login",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "center": [
                                {
                                    "logo": {
                                        "img": "data:image/webp;base64,UklGRpgDAABXRUJQVlA4TIwDAAA…UWmWq0fhNgGacPUnvxhbro3FeLM50kFYxRb3ia6Db6H8TAQ=="
                                    }
                                },
                                {
                                    "menu": [
                                        {
                                            "text": "HOME",
                                            "url": "https://preview.colorlib.com/theme/ogani/index.html",
                                            "content": [
                                                {
                                                    "banner1": {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/hero/banner.jpg",
                                                        "category": "Fresh Fruit",
                                                        "text": "Free Pickup and Delivery Available",
                                                        "button": "SHOP NOW",
                                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                    }
                                                },
                                                {
                                                    "slider": [
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-1.jpg",
                                                            "text": "fresh fruit",
                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                        },
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-2.jpg",
                                                            "text": "dried fruit",
                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                        },
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-3.jpg",
                                                            "text": "vegetables",
                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                        },
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-4.jpg",
                                                            "text": "drink fruit",
                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                        },
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-5.jpg",
                                                            "text": "drink fruits",
                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "featured spad": [
                                                        {
                                                            "text": "Featured Product",
                                                            "featured__controls": [
                                                                {
                                                                    "text": "All",
                                                                    "product": [
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "text": "Oranges",
                                                                    "product": [
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "text": "Fresh Meat",
                                                                    "product": [
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "text": "Vegetables",
                                                                    "product": [
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "text": "Fastfood",
                                                                    "product": [
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "price": "$30.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                {
                                                    "banner2": [
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/banner/xbanner-1.jpg.pagespeed.ic.aDN3QrExt6.webp"
                                                        },
                                                        {
                                                            "img": "https://preview.colorlib.com/theme/ogani/img/banner/xbanner-2.jpg.pagespeed.ic.-2eeuFVLcY.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "container": [
                                                        {
                                                            "text": "Latest Products",
                                                            "button": [
                                                                {
                                                                    "icon": "angle left"
                                                                },
                                                                {
                                                                    "icon": "angle right"
                                                                }
                                                            ],
                                                            "item": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "text": "Top Rateds Products",
                                                            "button": [
                                                                {
                                                                    "icon": "angle left"
                                                                },
                                                                {
                                                                    "icon": "angle right"
                                                                }
                                                            ],
                                                            "item": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "text": "Review Products",
                                                            "button": [
                                                                {
                                                                    "icon": "angle left"
                                                                },
                                                                {
                                                                    "icon": "angle right"
                                                                }
                                                            ],
                                                            "item": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                {
                                                    "Blog spad": [
                                                        {
                                                            "text": "From the Blog",
                                                            "blog": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Cooking tips make cooking simple",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "6 ways to prepare breakfast for 30",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Visit the clean farm in the US",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "text": "SHOP",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html",
                                            "content": [
                                                {
                                                    "banner": {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                                                        "text": "Organi Shop",
                                                        "option": {
                                                            "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                                            "text": "Shop"
                                                        }
                                                    }
                                                },
                                                {
                                                    "productspad": [
                                                        {
                                                            "left": {
                                                                "sidebar": [
                                                                    {
                                                                        "text": "Departement",
                                                                        "item": [
                                                                            {
                                                                                "text": "Fresh Meat",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Vegetables",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Fruit & Nut Gifts",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Fresh Berries",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Ocean Foods",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Butter & Eggs",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Fastfood",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Fresh Onion",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Papayaya & Crisps",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "text": "Oatmeal",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "text": "Price",
                                                                        "price-input": [
                                                                            {
                                                                                "minamout": {
                                                                                    "price": "$10"
                                                                                }
                                                                            },
                                                                            {
                                                                                "maxamout": {
                                                                                    "price": "$540"
                                                                                }
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "text": "color",
                                                                        "item-color": [
                                                                            {
                                                                                "label": "white",
                                                                                "text": "White"
                                                                            },
                                                                            {
                                                                                "label": "grey",
                                                                                "text": "Grey"
                                                                            },
                                                                            {
                                                                                "label": "red",
                                                                                "text": "Red"
                                                                            },
                                                                            {
                                                                                "label": "black",
                                                                                "text": "Black"
                                                                            },
                                                                            {
                                                                                "label": "blue",
                                                                                "text": "Blue"
                                                                            },
                                                                            {
                                                                                "label": "green",
                                                                                "text": "Green"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "text": "Popular Size",
                                                                        "item-size": [
                                                                            {
                                                                                "text": "Large"
                                                                            },
                                                                            {
                                                                                "text": "Medium"
                                                                            },
                                                                            {
                                                                                "text": "Small"
                                                                            },
                                                                            {
                                                                                "text": "Tiny"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "text": "Latest Products",
                                                                        "button": [
                                                                            {
                                                                                "icon": "angle left"
                                                                            },
                                                                            {
                                                                                "icon": "angle right"
                                                                            }
                                                                        ],
                                                                        "item": [
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                                                "text": "Crab Pool Security",
                                                                                "price": "$30.00",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        {
                                                            "right": [
                                                                {
                                                                    "product-discount": [
                                                                        {
                                                                            "id": "1",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "2",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "3",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "4",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-1.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "5",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "6",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=3.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "7",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "8",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "9",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "10",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=1.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "11",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "id": "12",
                                                                            "product-item": [
                                                                                {
                                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-3.jpg",
                                                                                    "discount-precent": "-20%"
                                                                                },
                                                                                {
                                                                                    "hover": [
                                                                                        {
                                                                                            "icon": "Heart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "retweet",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        },
                                                                                        {
                                                                                            "icon": "Shopping-cart",
                                                                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "item-text": [
                                                                                        {
                                                                                            "text": "Dried Fruit"
                                                                                        },
                                                                                        {
                                                                                            "text": "Raisin n nuts"
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    "price": [
                                                                                        {
                                                                                            "before-discount": {
                                                                                                "text": "$36.00"
                                                                                            }
                                                                                        },
                                                                                        {
                                                                                            "after-discount": {
                                                                                                "text": "$30.00 "
                                                                                            }
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "filter-item": [
                                                                        {
                                                                            "text": "Sort By",
                                                                            "filter-sort": {
                                                                                "value": "0",
                                                                                "result": "Default"
                                                                            }

                                                                        },
                                                                        {
                                                                            "filter-found": {
                                                                                "total": "16",
                                                                                "text": "Product Found"
                                                                            }
                                                                        },
                                                                        {
                                                                            "filter-option": [
                                                                                {
                                                                                    "icon": "grid"
                                                                                },
                                                                                {
                                                                                    "icon": "ul"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "product": [
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-9.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-10.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-11.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-12.jpg",
                                                                            "text": "Crab Pool Security",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                                            "price": "$150.00",
                                                                            "icon-hover": [
                                                                                {
                                                                                    "icon": "Heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "retweet",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "Shopping-cart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "pagination": [
                                                                        {
                                                                            "icon": "Heart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                        },
                                                                        {
                                                                            "icon": "retweet",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                        },
                                                                        {
                                                                            "icon": "Shopping-cart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "text": "PAGES",
                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#",
                                            "dropdown": [
                                                {
                                                    "text": "Shop Details",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-details.html",
                                                    "content": [
                                                        {
                                                            "banner": {
                                                                "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                                                                "text": "Vegetable's Package",
                                                                "option": [
                                                                    {
                                                                        "Home": "https://preview.colorlib.com/theme/ogani/index.html"
                                                                    },
                                                                    {
                                                                        "vegetables": "https://preview.colorlib.com/theme/ogani/index.html"
                                                                    },
                                                                    {
                                                                        "text": "Vegetable's Package"
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        {
                                                            "Product-details": [
                                                                {
                                                                    "pic-item": {
                                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/details/product-details-4.jpg",
                                                                        "pic-slider": [
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRvwGAABXRUJQVlA4IPAGAAD…fgobvbjuakIek4soOnyBbkOe9F1xrS5W4yK+TVPYAAAAAAAA="
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRiYIAABXRUJQVlA4IBoIAAD…REC8TU6ePJKS9JXtgS1Bc/sGnjgA5N70+yAAlKhMGAAAAAAAA"
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRrAGAABXRUJQVlA4IKQGAAB…dSJcyIIkMdOX1B5i2e5a0cjq2I7cSABeE38IWdAAAAAAAAA=="
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRkQFAABXRUJQVlA4IDgFAAB…aeH4tq62Q++PQW67PSP30OgbF8PlhAZsBxEMBONdfHs+AAAAA"
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRvwGAABXRUJQVlA4IPAGAAD…fgobvbjuakIek4soOnyBbkOe9F1xrS5W4yK+TVPYAAAAAAAA="
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRiYIAABXRUJQVlA4IBoIAAD…REC8TU6ePJKS9JXtgS1Bc/sGnjgA5N70+yAAlKhMGAAAAAAAA"
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRrAGAABXRUJQVlA4IKQGAAB…dSJcyIIkMdOX1B5i2e5a0cjq2I7cSABeE38IWdAAAAAAAAA=="
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRkQFAABXRUJQVlA4IDgFAAB…aeH4tq62Q++PQW67PSP30OgbF8PlhAZsBxEMBONdfHs+AAAAA"
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRvwGAABXRUJQVlA4IPAGAAD…fgobvbjuakIek4soOnyBbkOe9F1xrS5W4yK+TVPYAAAAAAAA="
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRiYIAABXRUJQVlA4IBoIAAD…REC8TU6ePJKS9JXtgS1Bc/sGnjgA5N70+yAAlKhMGAAAAAAAA"
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRrAGAABXRUJQVlA4IKQGAAB…dSJcyIIkMdOX1B5i2e5a0cjq2I7cSABeE38IWdAAAAAAAAA=="
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRkQFAABXRUJQVlA4IDgFAAB…aeH4tq62Q++PQW67PSP30OgbF8PlhAZsBxEMBONdfHs+AAAAA"
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "text": [
                                                                        {
                                                                            "tittle": "Vegetable's Package"
                                                                        },
                                                                        {
                                                                            "rating": [
                                                                                {
                                                                                    "icon": "star"
                                                                                },
                                                                                {
                                                                                    "icon": "star"
                                                                                },
                                                                                {
                                                                                    "icon": "star"
                                                                                },
                                                                                {
                                                                                    "icon": "star"
                                                                                },
                                                                                {
                                                                                    "icon": "half star"
                                                                                },
                                                                                {
                                                                                    "text": "18 reviews"
                                                                                }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "price": "$50.00"
                                                                        },
                                                                        {
                                                                            "descriptions": "Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Vestibulum ac diam sit amet quamvehicula elementum sed sit amet dui."
                                                                        },
                                                                        {
                                                                            "quantity": [
                                                                                {
                                                                                    "button": "-"
                                                                                },
                                                                                {
                                                                                    "value": "1"
                                                                                },
                                                                                {
                                                                                    "button": "+"
                                                                                },
                                                                                {
                                                                                    "button": "ADD TO CARD",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                                },
                                                                                {
                                                                                    "icon": "heart",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                                }
                                                                            ]

                                                                        },
                                                                        {
                                                                            "details": {
                                                                                "Availability": "In Stock",
                                                                                "Shipping": "01 day shipping. Free pickup today",
                                                                                "Weight": "0.5 kg",
                                                                                "Share on": [
                                                                                    {
                                                                                        "icon": "facebook",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "icon": "twitter",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "icon": "instagram",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "icon": "pinterest",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "product-tab": [
                                                                        {
                                                                            "nav-tab": [
                                                                                {
                                                                                    "text": "Description",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#tabs-1",
                                                                                    "content": {
                                                                                        "tittle": "Products Infomation",
                                                                                        "fill": "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Pellentesque in ipsum id orci porta dapibus. Proin eget tortor risus. Vivamus suscipit tortor eget felis porttitor volutpat."
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "text": "Information",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#tabs-2",
                                                                                    "content": {
                                                                                        "tittle": "Products Infomation",
                                                                                        "fill": "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Pellentesque in ipsum id orci porta dapibus. Proin eget tortor risus. Vivamus suscipit tortor eget felis porttitor volutpat."
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "text": "Riviews(1)",
                                                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#tabs-3",
                                                                                    "content": {
                                                                                        "tittle": "Products Infomation",
                                                                                        "fill": "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Pellentesque in ipsum id orci porta dapibus. Proin eget tortor risus. Vivamus suscipit tortor eget felis porttitor volutpat."
                                                                                    }
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "Related-product": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "icon-hover": [
                                                                        {
                                                                            "icon": "Heart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "retweet",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "Shopping-cart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "icon-hover": [
                                                                        {
                                                                            "icon": "Heart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "retweet",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "Shopping-cart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "icon-hover": [
                                                                        {
                                                                            "icon": "Heart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "retweet",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "Shopping-cart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                                                    "text": "Crab Pool Security",
                                                                    "price": "$30.00",
                                                                    "icon-hover": [
                                                                        {
                                                                            "icon": "Heart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "retweet",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        },
                                                                        {
                                                                            "icon": "Shopping-cart",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                {
                                                    "text": "Shoping Cart",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shoping-cart.html",
                                                    "content": [
                                                        {
                                                            "banner": {
                                                                "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                                                                "text": "Shopping Cart",
                                                                "option": {
                                                                    "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                                                    "text": "Shop"
                                                                }
                                                            }
                                                        },
                                                        {
                                                            "top": {
                                                                "tabel": [
                                                                    {
                                                                        "head": [
                                                                            {
                                                                                "text": "Product"
                                                                            },
                                                                            {
                                                                                "text": "Price"
                                                                            },
                                                                            {
                                                                                "text": "Quantity"
                                                                            },
                                                                            {
                                                                                "text": "Total"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "body": [
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRsAFAABXRUJQVlA4ILQFAAD…F252VnYKN7bEAQyMi6KgdbBApUJESf7Tg1RTpU0AAAAAAAA==",
                                                                                "product": "Vegetable's Package",
                                                                                "price": "$55.00",
                                                                                "quantity": [
                                                                                    {
                                                                                        "button": "-"
                                                                                    },
                                                                                    {
                                                                                        "value": "1"
                                                                                    },
                                                                                    {
                                                                                        "button": "+"
                                                                                    }
                                                                                ],
                                                                                "Total": "$110.00",
                                                                                "icon": "close"
                                                                            },
                                                                            {
                                                                                "img": "data:image/webp;base64,UklGRiYFAABXRUJQVlA4IBoFAAB…yvHSVY+cwiedQgWL44YzsjxYGR349Sn8bLREYT2AlhAAAAAAA",
                                                                                "product": "Vegetable's Package",
                                                                                "price": "$39.00",
                                                                                "quantity": [
                                                                                    {
                                                                                        "button": "-"
                                                                                    },
                                                                                    {
                                                                                        "value": "1"
                                                                                    },
                                                                                    {
                                                                                        "button": "+"
                                                                                    }
                                                                                ],
                                                                                "Total": "$39.99",
                                                                                "icon": "close"
                                                                            },
                                                                            {
                                                                                "img": "ata:image/webp;base64,UklGRtADAABXRUJQVlA4IMQDAAB…UNAwaNn5fw/clEzfd+KIM7JVauEgoKeJgFz2wZgIAd74AAAAA",
                                                                                "product": "Vegetable's Package",
                                                                                "price": "$69.00",
                                                                                "quantity": [
                                                                                    {
                                                                                        "button": "-"
                                                                                    },
                                                                                    {
                                                                                        "value": "1"
                                                                                    },
                                                                                    {
                                                                                        "button": "+"
                                                                                    }
                                                                                ],
                                                                                "Total": "$69.99",
                                                                                "icon": "close"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        {
                                                            "bottom": [
                                                                {
                                                                    "shoppingcart-btn": [
                                                                        {
                                                                            "left": {
                                                                                "text": "CONTINUE Shopping"
                                                                            }
                                                                        },
                                                                        {
                                                                            "right": {
                                                                                "icon": "loading",
                                                                                "text": "UPDATE CART"
                                                                            }
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "shopping-continue": {
                                                                        "text": "Discount Codes",
                                                                        "action": {
                                                                            "placeholder": "Enter your coupon code",
                                                                            "button": "APPLY COUPON"
                                                                        }
                                                                    }
                                                                },
                                                                {
                                                                    "shopping-checkout": {
                                                                        "text": "Cart Total",
                                                                        "cart": {
                                                                            "subtotal": "$454.98",
                                                                            "total": "$454.98",
                                                                            "button": "PROCEED TO CHECKOUT"
                                                                        }
                                                                    }
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                {
                                                    "text": "Check Out ",
                                                    "url": "https://preview.colorlib.com/theme/ogani/checkout.html"
                                                },
                                                {
                                                    "text": "Blog Details",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog-details.html",
                                                    "content": [
                                                        {
                                                            "banner": {
                                                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/details/details-hero.jpg",
                                                                "text": "The Moment You Need To Remove Garlic From The Menu",
                                                                "author": "Machael Scofield",
                                                                "date": "January 14, 2019",
                                                                "comment": "8"
                                                            }
                                                        },
                                                        {
                                                            "blog-dettails-spad": [
                                                                {
                                                                    "left": {
                                                                        "sidebar": [
                                                                            {
                                                                                "placeholder": "Search...",
                                                                                "icon": "search"
                                                                            },
                                                                            {
                                                                                "text": "Categories",
                                                                                "item": [
                                                                                    {
                                                                                        "text": "All",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "text": "Beauty (20)",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "text": "Food (5)",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "text": "Life Style (9)",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                    },
                                                                                    {
                                                                                        "text": "Travel (10)",
                                                                                        "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                    }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "text": "Recent News",
                                                                                "item": [
                                                                                    {
                                                                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-1.jpg.pagespeed.ic.chNerr_ywP.webp",
                                                                                        "tittle": "09 Kinds Of Vegetables  Protect The Liver",
                                                                                        "date": "MAR 05, 2019"
                                                                                    },
                                                                                    {
                                                                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-2.jpg.pagespeed.ic.NSkfePc_bi.webp",
                                                                                        "tittle": "Tips You To Balance Nutrition Meal Day",
                                                                                        "date": "MAR 05, 2019"
                                                                                    },
                                                                                    {
                                                                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-3.jpg.pagespeed.ic.IUyecbWYrU.webp",
                                                                                        "tittle": "4 Principles Help You Lose Weight With Vegetables",
                                                                                        "date": "MAR 05, 2019"
                                                                                    }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "text": "Search By",
                                                                                "item": [
                                                                                    {
                                                                                        "text": "Apple"
                                                                                    },
                                                                                    {
                                                                                        "text": "Beauty"
                                                                                    },
                                                                                    {
                                                                                        "text": "Vegetables"
                                                                                    },
                                                                                    {
                                                                                        "text": "Fruit"
                                                                                    },
                                                                                    {
                                                                                        "text": "Healthy Food"
                                                                                    },
                                                                                    {
                                                                                        "text": "Lifestyle"
                                                                                    }
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                },
                                                                {
                                                                    "right": [
                                                                        {
                                                                            "details-text": {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/…ils/xdetails-pic.jpg.pagespeed.ic.iXGi5L-xRP.webp",
                                                                                "text": "Sed porttitor lectus nibh. Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Vivamus magna justo,"
                                                                            }
                                                                        },
                                                                        {
                                                                            "details-content": [
                                                                                {
                                                                                    "details-author": {
                                                                                        "pic": "https://preview.colorlib.com/theme/ogani/img/blog/…/xdetails-author.jpg.pagespeed.ic.PvwPsmLHih.webp",
                                                                                        "name": "Michael Scofield",
                                                                                        "status": "Admin"
                                                                                    }
                                                                                },
                                                                                {
                                                                                    "Detail-widget": {
                                                                                        "categories": "Food",
                                                                                        "Tags": "All, Trending, Cooking, Healthy Food, Life Style",
                                                                                        "sosmed": [
                                                                                            {
                                                                                                "icon": "facebook",
                                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                            },
                                                                                            {
                                                                                                "icon": "twitter",
                                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                            },
                                                                                            {
                                                                                                "icon": "google plus",
                                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                            },
                                                                                            {
                                                                                                "icon": "linkedin",
                                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                            },
                                                                                            {
                                                                                                "icon": "email",
                                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                                            }
                                                                                        ]
                                                                                    }
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "text": "Post You May Like",
                                                            "related-blog": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Cooking tips make cooking simple",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "6 ways to prepare breakfast for 30",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Visit the clean farm in the US",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "text": "BLOG",
                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html",
                                            "content": [
                                                {
                                                    "banner": {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                                                        "text": "Blog",
                                                        "option": {
                                                            "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                                            "text": "Shop"
                                                        }
                                                    }
                                                },
                                                {
                                                    "blog-spad": [
                                                        {
                                                            "left": {
                                                                "sidebar": [
                                                                    {
                                                                        "placeholder": "Search...",
                                                                        "icon": "search"
                                                                    },
                                                                    {
                                                                        "text": "Categories",
                                                                        "item": [
                                                                            {
                                                                                "text": "All",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                            },
                                                                            {
                                                                                "text": "Beauty (20)",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                            },
                                                                            {
                                                                                "text": "Food (5)",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                            },
                                                                            {
                                                                                "text": "Life Style (9)",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                            },
                                                                            {
                                                                                "text": "Travel (10)",
                                                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "text": "Recent News",
                                                                        "item": [
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-1.jpg.pagespeed.ic.chNerr_ywP.webp",
                                                                                "tittle": "09 Kinds Of Vegetables  Protect The Liver",
                                                                                "date": "MAR 05, 2019"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-2.jpg.pagespeed.ic.NSkfePc_bi.webp",
                                                                                "tittle": "Tips You To Balance Nutrition Meal Day",
                                                                                "date": "MAR 05, 2019"
                                                                            },
                                                                            {
                                                                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-3.jpg.pagespeed.ic.IUyecbWYrU.webp",
                                                                                "tittle": "4 Principles Help You Lose Weight With Vegetables",
                                                                                "date": "MAR 05, 2019"
                                                                            }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "text": "Search By",
                                                                        "item": [
                                                                            {
                                                                                "text": "Apple"
                                                                            },
                                                                            {
                                                                                "text": "Beauty"
                                                                            },
                                                                            {
                                                                                "text": "Vegetables"
                                                                            },
                                                                            {
                                                                                "text": "Fruit"
                                                                            },
                                                                            {
                                                                                "text": "Healthy Food"
                                                                            },
                                                                            {
                                                                                "text": "Lifestyle"
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        },
                                                        {
                                                            "right": [
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "6 ways to prepare breakfast for 30",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        },
                                                                        {
                                                                            "text": "READ MORE",
                                                                            "icon": "arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Visit the clean farm in the US",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        },
                                                                        {
                                                                            "text": "READ MORE",
                                                                            "icon": "arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Cooking tips make cooking simple",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        },
                                                                        {
                                                                            "text": "READ MORE",
                                                                            "icon": "arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Cooking tips make cooking simple",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        },
                                                                        {
                                                                            "text": "READ MORE",
                                                                            "icon": "arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "The Moment You Need To Remove Garlic From The Menu",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        },
                                                                        {
                                                                            "text": "READ MORE",
                                                                            "icon": "arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-6.jpg.pagespeed.ic.P_hTD59ZOA.webp",
                                                                    "blog_item_text": [
                                                                        {
                                                                            "icon": "calendar",
                                                                            "date": " May 4,2019"
                                                                        },
                                                                        {
                                                                            "icon": "comment",
                                                                            "value": "5"
                                                                        },
                                                                        {
                                                                            "text": "Cooking tips make cooking simple",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                                                        },
                                                                        {
                                                                            "text": "READ MORE",
                                                                            "icon": "arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    "pagination": [
                                                                        {
                                                                            "id": "1",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "id": "2",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "id": "3",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        },
                                                                        {
                                                                            "icon": "long arrow right",
                                                                            "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "text": "CONTACT",
                                            "url": "https://preview.colorlib.com/theme/ogani/contact.html",
                                            "contact": [
                                                {
                                                    "banner": {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                                                        "text": "Contact Us",
                                                        "option": {
                                                            "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                                            "text": "Contact Us"
                                                        }
                                                    }
                                                },
                                                {
                                                    "conatct-spad": [
                                                        {
                                                            "icon": "phone",
                                                            "text": "Phone",
                                                            "tell": "+01-3-8888-6868"
                                                        },
                                                        {
                                                            "icon": "pin",
                                                            "text": "Address",
                                                            "tell": "60-49 Road 11378 New York"
                                                        },
                                                        {
                                                            "icon": "clock",
                                                            "text": "Open Time",
                                                            "tell": "10:00 am to 23:00 pm"
                                                        },
                                                        {
                                                            "icon": "mail",
                                                            "text": "Email",
                                                            "tell": "hello@colorlib.com"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d49116.39176087041!2d-86.41867791216099!3d39.69977417971648!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x886ca48c841038a1%3A0x70cfba96bf847f0!2sPlainfield%2C%20IN%2C%20USA!5e0!3m2!1sen!2sbd!4v1586106673811!5m2!1sen!2sbd",
                                                    "map-inside": {
                                                        "icon": "pin",
                                                        "City": "New York",
                                                        "Phone": "+12-345-6789",
                                                        "address": "16 Creek Ave. Farmingdale, NY"
                                                    }
                                                },
                                                {
                                                    "text": "Leave Message",
                                                    "form": [
                                                        {
                                                            "placeholder": "Your Name"
                                                        },
                                                        {
                                                            "placeholder": "Your Email"
                                                        },
                                                        {
                                                            "placeholder": "Your Message"
                                                        },
                                                        {
                                                            "button":  "SEND MESSAGE"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "cart": [
                                        {
                                            "icon": "heart",
                                            "notif": "1",
                                            "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                        },
                                        {
                                            "icon": "Shopping Bag",
                                            "notif": "3",
                                            "url": "https://preview.colorlib.com/theme/ogani/#"
                                        },
                                        {
                                            "cart price": {
                                                "text": "item :",
                                                "price": "$150.00"
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "bottom": [
                                {
                                    "selection": {
                                        "icon": "bars",
                                        "text": "All Departements",
                                        "category": [
                                            {
                                                "Text": "Fresh Meat",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Vegetables",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Fruit & Nut Gifts",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Fresh Berries",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Ocean Foods",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Butter & Eggs",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Fastfood",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Fresh Onion",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Papayaya & Crips",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Oatmeal",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "Text": "Fresh Bananas",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    }
                                },
                                {
                                    "search form": [
                                        {
                                            "text": "All Categories",
                                            "icon": "carrot down"
                                        },
                                        {
                                            "placeholder": "What do u need?",
                                            "text": "SEARCH"
                                        }
                                    ]
                                },
                                {
                                    "telephone": {
                                        "icon": "phone",
                                        "number": "+65 11.188.888",
                                        "text": "support 24/7 time"
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "footer": [
                        {
                            "top": [
                                {
                                    "left": {
                                        "img": "data:image/webp;base64,UklGRpgDAABXRUJQVlA4TIwDAAAvdkAMEO/BJpJkK72vXvT4ZqS4w78Aam04jiRJarJ3X/C6wSD8N0lqto0kSak5fjws8o+QCI5hE9m2E36dOGS6bAJrWKJCBH0SkBQ86JkfCJ731Wu9DYoxhk1iYOGSWLi2AMTIUCbp2vbvvU4Zlu97fkrCV1AqChChRlVJEpY17VzODKoiVZlcTPof1Zj/kOHNnMe9fc+x9IOw1RQzNUVBYaC8NAIVKIrgiYj6/3UEbdu22tjRVkQIwcY5lHHsfHMOpv//w84phDxab/0Q0f8JQOGPP35D8ck1dvJ7Sp+/Fpw/57Od+JFSSh+/Kye3OeebPUnpDYCr55xzft6JL1p6i5usn+/Du5TSp5RS+vPpyOU+fEopfTyklNK/Oef7nPPVPiT5TvyVc77bj4NySCm9vs93jznni314LdLrlNL7+6ernHM+2Yfvyivl+mfO+RE7eRCvDym9ur7OOeeLvfhdvH+f0t+XOef8gN38Jl6l9xc55/xwuh/4fkjpx4d/cs755hQ72VtHki9edqfnl+enKO8nF0hycaZvyhaqfRHVqcSQpFMMZVdiAgt9h/LGBBa7okjdVmD8JdqFK21R57mybDoSaiy/QgxcbQsGri7zR9hXoNmuWVhxOjLwuHPOrYokGYStEdrNLNWlB9CaoLBT2qC5HmrTT7ZkErMINei26qha6DEoTnFUB1QOohMcarDfyCoLjvcKI4CO6oDKPUl6ODGvCSI021DtCuAUA8AqM2pbMWEUbFZMgSTtJp2yoHRQHICgxGpBdGiVYYUZBbstjDIVRSUAkdKj9kCSAYAX8xo44beYlLEICoFOcQpLj8zCApgEmzVR0GzglK6OUUythnIAEJVhDYxg/O8ZlAYAgnCr4IWrNyvDFraWEzOkFWxXdYJjNaOYolbxQKc4xUhf0lKOSq+MqzCJ0NQalKVoUGYgKmyE6kpGpXxZ1wSSnGu1CmOJU0YAQTF1lgpsV6EXdJWwKK6gp9oAsEpoa7SsOa7DLNQag0J7JAbFAkBUuLQVpipLhTZsgUWh6wG0hmpoBazCYFrRLgVe6Y57wXYdxk1iUFYOUBuvkPTOeeoAIuWM45MyVYDbAl2FAUdjOFIMYFLGgqj4GnETxLAiDChs3boAIChtAbxgrACzCRpbZFuUD74smAboKReUWmWq0fhNgGacPUnvxhbro3FeLM50kFYxRb3ia6Db6H8TAQ==",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html",
                                        "address": "60-49 Road 11378 New York",
                                        "phone": "+65 11.188.888",
                                        "email": "hello@colorlib.com"
                                    }

                                },
                                {
                                    "center": [
                                        {
                                            "text": "Useful Links",
                                            "link": [
                                                {
                                                    "text": "About Us",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "About Our Shop",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Secure Shopping",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Delivery infomation",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Privacy Policy",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Our Sitemap",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Who We Are",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Our Service",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Project",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Contact",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Innovation",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "text": "Testimonials",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "right": [
                                        {
                                            "text": "Join Our Newsletter Now",
                                            "isi": "Get E-mail updates about our latest shop and special offers."
                                        },
                                        {
                                            "placeholder": "Enter your mail",
                                            "button": "Subscribe"
                                        },
                                        {
                                            "sosmed": [
                                                {
                                                    "icon": "facebook",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "icon": "instagram",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                },
                                                {
                                                    "icon": "pinterest",
                                                    "url": "https://preview.colorlib.com/theme/ogani/#"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "bottom": [
                                {
                                    "left": {
                                        "text": "Copyright ©2022 All rights reserved | This template is made with ",
                                        "icon": "heart",
                                        "by": "Colorlib",
                                        "url": "https://colorlib.com/"
                                    }
                                },
                                {
                                    "right": {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/xpayment-item.png.pagespeed.ic.fk3ziISga0.webp"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Slider(Resource):
    def get(self):
        return {
            "data": {
                "slider": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-1.jpg",
                        "text": "fresh fruit",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-2.jpg",
                        "text": "dried fruit",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-3.jpg",
                        "text": "vegetables",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-4.jpg",
                        "text": "drink fruit",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/categories/cat-5.jpg",
                        "text": "drink fruits",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    }
                ]
            }
        }


class Lates_products(Resource):
    def get(self):
        return {
            "data": {
                "text": "Latest Products",
                "button": [
                    {
                        "icon": "angle left"
                    },
                    {
                        "icon": "angle right"
                    }
                ],
                "item": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    }
                ]
            }
        }


class Toprateds_products(Resource):
    def get(self):
        return{
            "data": {
                "text": "Top Rateds Products",
                "button": [
                    {
                        "icon": "angle left"
                    },
                    {
                        "icon": "angle right"
                    }
                ],
                "item": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    }
                ]
            }
        }


class Review_products(Resource):
    def get(self):
        return{
            "data":  {
                "text": "Review Products",
                "button": [
                    {
                        "icon": "angle left"
                    },
                    {
                        "icon": "angle right"
                    }
                ],
                "item": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    }
                ]
            }
        }


class Menu_blogspand(Resource):
    def get(self):
        return{
            "data": {
                "Blog spad": [
                    {
                        "text": "From the Blog",
                        "blog": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                                "blog_item_text": [
                                    {
                                        "icon": "calendar",
                                        "date": " May 4,2019"
                                    },
                                    {
                                        "icon": "comment",
                                        "value": "5"
                                    },
                                    {
                                        "text": "Cooking tips make cooking simple",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    },
                                    {
                                        "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    }
                                ]
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                                "blog_item_text": [
                                    {
                                        "icon": "calendar",
                                        "date": " May 4,2019"
                                    },
                                    {
                                        "icon": "comment",
                                        "value": "5"
                                    },
                                    {
                                        "text": "6 ways to prepare breakfast for 30",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    },
                                    {
                                        "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    }
                                ]
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                                "blog_item_text": [
                                    {
                                        "icon": "calendar",
                                        "date": " May 4,2019"
                                    },
                                    {
                                        "icon": "comment",
                                        "value": "5"
                                    },
                                    {
                                        "text": "Visit the clean farm in the US",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    },
                                    {
                                        "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Feuturedspad(Resource):
    def get(self):
        return {
            "data": {
                "featured spad": [
                    {
                        "text": "Featured Product",
                        "featured__controls": [
                            {
                                "text": "All",
                                "product": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "text": "Oranges",
                                "product": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "text": "Fresh Meat",
                                "product": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "text": "Vegetables",
                                "product": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "text": "Fastfood",
                                "product": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                        "text": "Crab Pool Security",
                                        "price": "$30.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Container(Resource):
    def get(self):
        return {
            "data":  {
                "container": [
                    {
                        "text": "Latest Products",
                        "button": [
                            {
                                "icon": "angle left"
                            },
                            {
                                "icon": "angle right"
                            }
                        ],
                        "item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            }
                        ]
                    },
                    {
                        "text": "Top Rateds Products",
                        "button": [
                            {
                                "icon": "angle left"
                            },
                            {
                                "icon": "angle right"
                            }
                        ],
                        "item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            }
                        ]
                    },
                    {
                        "text": "Review Products",
                        "button": [
                            {
                                "icon": "angle left"
                            },
                            {
                                "icon": "angle right"
                            }
                        ],
                        "item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                "text": "Crab Pool Security",
                                "price": "$30.00",
                                "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                            }
                        ]
                    }
                ]
            }
        }


class Menublog_spand(Resource):
    def get(self):
        return {
            "data": {
                "Blog spad": [
                    {
                        "text": "From the Blog",
                        "blog": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                                "blog_item_text": [
                                    {
                                        "icon": "calendar",
                                        "date": " May 4,2019"
                                    },
                                    {
                                        "icon": "comment",
                                        "value": "5"
                                    },
                                    {
                                        "text": "Cooking tips make cooking simple",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    },
                                    {
                                        "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    }
                                ]
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                                "blog_item_text": [
                                    {
                                        "icon": "calendar",
                                        "date": " May 4,2019"
                                    },
                                    {
                                        "icon": "comment",
                                        "value": "5"
                                    },
                                    {
                                        "text": "6 ways to prepare breakfast for 30",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    },
                                    {
                                        "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    }
                                ]
                            },
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                                "blog_item_text": [
                                    {
                                        "icon": "calendar",
                                        "date": " May 4,2019"
                                    },
                                    {
                                        "icon": "comment",
                                        "value": "5"
                                    },
                                    {
                                        "text": "Visit the clean farm in the US",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    },
                                    {
                                        "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat",
                                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Shop(Resource):
    def get(self):
        return {
            "data": {
                "text": "SHOP",
                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html",
                "content": [
                    {
                        "banner": {
                            "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                            "text": "Organi Shop",
                            "option": {
                                "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                "text": "Shop"
                            }
                        }
                    },
                    {
                        "productspad": [
                            {
                                "left": {
                                    "sidebar": [
                                        {
                                            "text": "Departement",
                                            "item": [
                                                {
                                                    "text": "Fresh Meat",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Vegetables",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Fruit & Nut Gifts",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Fresh Berries",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Ocean Foods",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Butter & Eggs",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Fastfood",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Fresh Onion",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Papayaya & Crisps",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "text": "Oatmeal",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Price",
                                            "price-input": [
                                                {
                                                    "minamout": {
                                                        "price": "$10"
                                                    }
                                                },
                                                {
                                                    "maxamout": {
                                                        "price": "$540"
                                                    }
                                                }
                                            ]
                                        },
                                        {
                                            "text": "color",
                                            "item-color": [
                                                {
                                                    "label": "white",
                                                    "text": "White"
                                                },
                                                {
                                                    "label": "grey",
                                                    "text": "Grey"
                                                },
                                                {
                                                    "label": "red",
                                                    "text": "Red"
                                                },
                                                {
                                                    "label": "black",
                                                    "text": "Black"
                                                },
                                                {
                                                    "label": "blue",
                                                    "text": "Blue"
                                                },
                                                {
                                                    "label": "green",
                                                    "text": "Green"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Popular Size",
                                            "item-size": [
                                                {
                                                    "text": "Large"
                                                },
                                                {
                                                    "text": "Medium"
                                                },
                                                {
                                                    "text": "Small"
                                                },
                                                {
                                                    "text": "Tiny"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Latest Products",
                                            "button": [
                                                {
                                                    "icon": "angle left"
                                                },
                                                {
                                                    "icon": "angle right"
                                                }
                                            ],
                                            "item": [
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                                    "text": "Crab Pool Security",
                                                    "price": "$30.00",
                                                    "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            {
                                "right": [
                                    {
                                        "product-discount": [
                                            {
                                                "id": "1",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "2",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "3",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "4",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-1.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "5",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "6",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=3.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "7",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "8",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "9",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "10",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=1.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "11",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "12",
                                                "product-item": [
                                                    {
                                                        "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-3.jpg",
                                                        "discount-precent": "-20%"
                                                    },
                                                    {
                                                        "hover": [
                                                            {
                                                                "icon": "Heart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "retweet",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            },
                                                            {
                                                                "icon": "Shopping-cart",
                                                                "url": "https://preview.colorlib.com/theme/ogani/#"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "item-text": [
                                                            {
                                                                "text": "Dried Fruit"
                                                            },
                                                            {
                                                                "text": "Raisin n nuts"
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "price": [
                                                            {
                                                                "before-discount": {
                                                                    "text": "$36.00"
                                                                }
                                                            },
                                                            {
                                                                "after-discount": {
                                                                    "text": "$30.00 "
                                                                }
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "filter-item": [
                                            {
                                                "text": "Sort By",
                                                "filter-sort": {
                                                    "value": "0",
                                                    "result": "Default"
                                                }

                                            },
                                            {
                                                "filter-found": {
                                                    "total": "16",
                                                    "text": "Product Found"
                                                }
                                            },
                                            {
                                                "filter-option": [
                                                    {
                                                        "icon": "grid"
                                                    },
                                                    {
                                                        "icon": "ul"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "product": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-9.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-10.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-11.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            },
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-12.jpg",
                                                "text": "Crab Pool Security",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                                "price": "$150.00",
                                                "icon-hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "pagination": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Shop_departemint(Resource):
    def get(self):
        return {
            "data":  {
                "text": "Departement",
                "item": [
                    {
                        "text": "Fresh Meat",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Vegetables",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Fruit & Nut Gifts",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Fresh Berries",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Ocean Foods",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Butter & Eggs",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Fastfood",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Fresh Onion",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Papayaya & Crisps",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    },
                    {
                        "text": "Oatmeal",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                    }
                ]
            }
        }


class Shop_price(Resource):
    def get(self):
        return {
            "data": {
                "text": "Price",
                "price-input": [
                    {
                        "minamout": {
                            "price": "$10"
                        }
                    },
                    {
                        "maxamout": {
                            "price": "$540"
                        }
                    }
                ]
            }
        }


class Shop_color(Resource):
    def get(self):
        return {
            "data": {
                "text": "color",
                "item-color": [
                    {
                        "label": "white",
                        "text": "White"
                    },
                    {
                        "label": "grey",
                        "text": "Grey"
                    },
                    {
                        "label": "red",
                        "text": "Red"
                    },
                    {
                        "label": "black",
                        "text": "Black"
                    },
                    {
                        "label": "blue",
                        "text": "Blue"
                    },
                    {
                        "label": "green",
                        "text": "Green"
                    }
                ]
            }
        }


class ShopLates_products(Resource):
    def get(self):
        return {
            "data": {
                "text": "Latest Products",
                "button": [
                    {
                        "icon": "angle left"
                    },
                    {
                        "icon": "angle right"
                    }
                ],
                "item": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "url": "https://preview.colorlib.com/theme/ogani/index.html#"
                    }
                ]
            }
        }


class Shoproduts_discount(Resource):
    def get(self):
        return {
            "data": {
                "product-discount": [
                    {
                        "id": "1",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "2",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "3",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "4",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-1.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "5",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "6",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=3.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "7",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "8",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "9",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "10",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=1.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "11",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "id": "12",
                        "product-item": [
                            {
                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-3.jpg",
                                "discount-precent": "-20%"
                            },
                            {
                                "hover": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                    }
                                ]
                            },
                            {
                                "item-text": [
                                    {
                                        "text": "Dried Fruit"
                                    },
                                    {
                                        "text": "Raisin n nuts"
                                    }
                                ]
                            },
                            {
                                "price": [
                                    {
                                        "before-discount": {
                                            "text": "$36.00"
                                        }
                                    },
                                    {
                                        "after-discount": {
                                            "text": "$30.00 "
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Shopfilter_item(Resource):
    def get(self):
        return {
            "data": {
                "filter-item": [
                    {
                        "text": "Sort By",
                        "filter-sort": {
                            "value": "0",
                            "result": "Default"
                        }

                    },
                    {
                        "filter-found": {
                            "total": "16",
                            "text": "Product Found"
                        }
                    },
                    {
                        "filter-option": [
                            {
                                "icon": "grid"
                            },
                            {
                                "icon": "ul"
                            }
                        ]
                    }
                ]
            }
        }


class Shopproduct(Resource):
    def get(self):
        return {
            "data": {
                "product": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-9.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-10.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-11.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-12.jpg",
                        "text": "Crab Pool Security",
                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                        "price": "$150.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                            }
                        ]
                    }
                ]
            }
        }


class Shop_size(Resource):
    def get(self):
        return {
            "data": {
                "text": "Popular Size",
                "item-size": [
                    {
                        "text": "Large"
                    },
                    {
                        "text": "Medium"
                    },
                    {
                        "text": "Small"
                    },
                    {
                        "text": "Tiny"
                    }
                ]
            }
        }


class Productspad(Resource):
    def get(self):
        return {
            "data": {
                "productspad": [
                    {
                        "left": {
                            "sidebar": [
                                {
                                    "text": "Departement",
                                    "item": [
                                        {
                                            "text": "Fresh Meat",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Vegetables",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Fruit & Nut Gifts",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Fresh Berries",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Ocean Foods",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Butter & Eggs",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Fastfood",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Fresh Onion",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Papayaya & Crisps",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "text": "Oatmeal",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        }
                                    ]
                                },
                                {
                                    "text": "Price",
                                    "price-input": [
                                        {
                                            "minamout": {
                                                "price": "$10"
                                            }
                                        },
                                        {
                                            "maxamout": {
                                                "price": "$540"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "text": "color",
                                    "item-color": [
                                        {
                                            "label": "white",
                                            "text": "White"
                                        },
                                        {
                                            "label": "grey",
                                            "text": "Grey"
                                        },
                                        {
                                            "label": "red",
                                            "text": "Red"
                                        },
                                        {
                                            "label": "black",
                                            "text": "Black"
                                        },
                                        {
                                            "label": "blue",
                                            "text": "Blue"
                                        },
                                        {
                                            "label": "green",
                                            "text": "Green"
                                        }
                                    ]
                                },
                                {
                                    "text": "Popular Size",
                                    "item-size": [
                                        {
                                            "text": "Large"
                                        },
                                        {
                                            "text": "Medium"
                                        },
                                        {
                                            "text": "Small"
                                        },
                                        {
                                            "text": "Tiny"
                                        }
                                    ]
                                },
                                {
                                    "text": "Latest Products",
                                    "button": [
                                        {
                                            "icon": "angle left"
                                        },
                                        {
                                            "icon": "angle right"
                                        }
                                    ],
                                    "item": [
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-1.jpg.pagespeed.ic.dQgcajStX5.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-2.jpg.pagespeed.ic.NOJHmb0hZw.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/latest-product/xlp-3.jpg.pagespeed.ic.eEz5Jo7-Qa.webp",
                                            "text": "Crab Pool Security",
                                            "price": "$30.00",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                        }
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "right": [
                            {
                                "product-discount": [
                                    {
                                        "id": "1",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "2",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "3",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "4",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-1.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "5",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "6",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=3.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "7",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-4.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "8",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-5.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "9",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-6.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "10",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-=1.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "11",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-2.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "id": "12",
                                        "product-item": [
                                            {
                                                "img": "https://preview.colorlib.com/theme/ogani/img/product/discount/pd-3.jpg",
                                                "discount-precent": "-20%"
                                            },
                                            {
                                                "hover": [
                                                    {
                                                        "icon": "Heart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "retweet",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    },
                                                    {
                                                        "icon": "Shopping-cart",
                                                        "url": "https://preview.colorlib.com/theme/ogani/#"
                                                    }
                                                ]
                                            },
                                            {
                                                "item-text": [
                                                    {
                                                        "text": "Dried Fruit"
                                                    },
                                                    {
                                                        "text": "Raisin n nuts"
                                                    }
                                                ]
                                            },
                                            {
                                                "price": [
                                                    {
                                                        "before-discount": {
                                                            "text": "$36.00"
                                                        }
                                                    },
                                                    {
                                                        "after-discount": {
                                                            "text": "$30.00 "
                                                        }
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "filter-item": [
                                    {
                                        "text": "Sort By",
                                        "filter-sort": {
                                            "value": "0",
                                            "result": "Default"
                                        }

                                    },
                                    {
                                        "filter-found": {
                                            "total": "16",
                                            "text": "Product Found"
                                        }
                                    },
                                    {
                                        "filter-option": [
                                            {
                                                "icon": "grid"
                                            },
                                            {
                                                "icon": "ul"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "product": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-4.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-5.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-6.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-8.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-9.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-10.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-11.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-12.jpg",
                                        "text": "Crab Pool Security",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#",
                                        "price": "$150.00",
                                        "icon-hover": [
                                            {
                                                "icon": "Heart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "retweet",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            },
                                            {
                                                "icon": "Shopping-cart",
                                                "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "pagination": [
                                    {
                                        "icon": "Heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                    },
                                    {
                                        "icon": "retweet",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                    },
                                    {
                                        "icon": "Shopping-cart",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-grid.html#"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Pages(Resource):
    def get(self):
        return {
            "data": {
                "text": "CONTACT",
                "url": "https://preview.colorlib.com/theme/ogani/contact.html",
                "contact": [
                    {
                        "banner": {
                            "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                            "text": "Contact Us",
                            "option": {
                                "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                "text": "Contact Us"
                            }
                        }
                    },
                    {
                        "conatct-spad": [
                            {
                                "icon": "phone",
                                "text": "Phone",
                                "tell": "+01-3-8888-6868"
                            },
                            {
                                "icon": "pin",
                                "text": "Address",
                                "tell": "60-49 Road 11378 New York"
                            },
                            {
                                "icon": "clock",
                                "text": "Open Time",
                                "tell": "10:00 am to 23:00 pm"
                            },
                            {
                                "icon": "mail",
                                "text": "Email",
                                "tell": "hello@colorlib.com"
                            }
                        ]
                    },
                    {
                        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d49116.39176087041!2d-86.41867791216099!3d39.69977417971648!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x886ca48c841038a1%3A0x70cfba96bf847f0!2sPlainfield%2C%20IN%2C%20USA!5e0!3m2!1sen!2sbd!4v1586106673811!5m2!1sen!2sbd",
                        "map-inside": {
                            "icon": "pin",
                            "City": "New York",
                            "Phone": "+12-345-6789",
                            "address": "16 Creek Ave. Farmingdale, NY"
                        }
                    },
                    {
                        "text": "Leave Message",
                        "form": [
                            {
                                "placeholder": "Your Name"
                            },
                            {
                                "placeholder": "Your Email"
                            },
                            {
                                "placeholder": "Your Message"
                            },
                            {
                                "button":  "SEND MESSAGE"
                            }
                        ]
                    }
                ]
            }
        }


class Pagesproduct_detail(Resource):
    def get(self):
        return {
            "data": {
                "Product-details": [
                    {
                        "pic-item": {
                            "img": "https://preview.colorlib.com/theme/ogani/img/product/details/product-details-4.jpg",
                            "pic-slider": [
                                {
                                    "img": "data:image/webp;base64,UklGRvwGAABXRUJQVlA4IPAGAAD…fgobvbjuakIek4soOnyBbkOe9F1xrS5W4yK+TVPYAAAAAAAA="
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRiYIAABXRUJQVlA4IBoIAAD…REC8TU6ePJKS9JXtgS1Bc/sGnjgA5N70+yAAlKhMGAAAAAAAA"
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRrAGAABXRUJQVlA4IKQGAAB…dSJcyIIkMdOX1B5i2e5a0cjq2I7cSABeE38IWdAAAAAAAAA=="
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRkQFAABXRUJQVlA4IDgFAAB…aeH4tq62Q++PQW67PSP30OgbF8PlhAZsBxEMBONdfHs+AAAAA"
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRvwGAABXRUJQVlA4IPAGAAD…fgobvbjuakIek4soOnyBbkOe9F1xrS5W4yK+TVPYAAAAAAAA="
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRiYIAABXRUJQVlA4IBoIAAD…REC8TU6ePJKS9JXtgS1Bc/sGnjgA5N70+yAAlKhMGAAAAAAAA"
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRrAGAABXRUJQVlA4IKQGAAB…dSJcyIIkMdOX1B5i2e5a0cjq2I7cSABeE38IWdAAAAAAAAA=="
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRkQFAABXRUJQVlA4IDgFAAB…aeH4tq62Q++PQW67PSP30OgbF8PlhAZsBxEMBONdfHs+AAAAA"
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRvwGAABXRUJQVlA4IPAGAAD…fgobvbjuakIek4soOnyBbkOe9F1xrS5W4yK+TVPYAAAAAAAA="
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRiYIAABXRUJQVlA4IBoIAAD…REC8TU6ePJKS9JXtgS1Bc/sGnjgA5N70+yAAlKhMGAAAAAAAA"
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRrAGAABXRUJQVlA4IKQGAAB…dSJcyIIkMdOX1B5i2e5a0cjq2I7cSABeE38IWdAAAAAAAAA=="
                                },
                                {
                                    "img": "data:image/webp;base64,UklGRkQFAABXRUJQVlA4IDgFAAB…aeH4tq62Q++PQW67PSP30OgbF8PlhAZsBxEMBONdfHs+AAAAA"
                                }
                            ]
                        }
                    },
                    {
                        "text": [
                            {
                                "tittle": "Vegetable's Package"
                            },
                            {
                                "rating": [
                                    {
                                        "icon": "star"
                                    },
                                    {
                                        "icon": "star"
                                    },
                                    {
                                        "icon": "star"
                                    },
                                    {
                                        "icon": "star"
                                    },
                                    {
                                        "icon": "half star"
                                    },
                                    {
                                        "text": "18 reviews"
                                    }
                                ]
                            },
                            {
                                "price": "$50.00"
                            },
                            {
                                "descriptions": "Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Vestibulum ac diam sit amet quamvehicula elementum sed sit amet dui."
                            },
                            {
                                "quantity": [
                                    {
                                        "button": "-"
                                    },
                                    {
                                        "value": "1"
                                    },
                                    {
                                        "button": "+"
                                    },
                                    {
                                        "button": "ADD TO CARD",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                    },
                                    {
                                        "icon": "heart",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                    }
                                ]

                            },
                            {
                                "details": {
                                    "Availability": "In Stock",
                                    "Shipping": "01 day shipping. Free pickup today",
                                    "Weight": "0.5 kg",
                                    "Share on": [
                                        {
                                            "icon": "facebook",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                        },
                                        {
                                            "icon": "twitter",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                        },
                                        {
                                            "icon": "instagram",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                        },
                                        {
                                            "icon": "pinterest",
                                            "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    {
                        "product-tab": [
                            {
                                "nav-tab": [
                                    {
                                        "text": "Description",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#tabs-1",
                                        "content": {
                                            "tittle": "Products Infomation",
                                            "fill": "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Pellentesque in ipsum id orci porta dapibus. Proin eget tortor risus. Vivamus suscipit tortor eget felis porttitor volutpat."
                                        }
                                    },
                                    {
                                        "text": "Information",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#tabs-2",
                                        "content": {
                                            "tittle": "Products Infomation",
                                            "fill": "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Pellentesque in ipsum id orci porta dapibus. Proin eget tortor risus. Vivamus suscipit tortor eget felis porttitor volutpat."
                                        }
                                    },
                                    {
                                        "text": "Riviews(1)",
                                        "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#tabs-3",
                                        "content": {
                                            "tittle": "Products Infomation",
                                            "fill": "Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Pellentesque in ipsum id orci porta dapibus. Proin eget tortor risus. Vivamus suscipit tortor eget felis porttitor volutpat."
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Pagesrelated_product(Resource):
    def get(self):
        return {
            "pages": {
                "Related-product": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-1.jpg",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-2.jpg",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-3.jpg",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/featured/feature-7.jpg",
                        "text": "Crab Pool Security",
                        "price": "$30.00",
                        "icon-hover": [
                            {
                                "icon": "Heart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "retweet",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            },
                            {
                                "icon": "Shopping-cart",
                                "url": "https://preview.colorlib.com/theme/ogani/shop-details.html#"
                            }
                        ]
                    }
                ]
            }
        }


class Pageshoping_chart(Resource):
    def get(self):
        return {
            "data": {
                "bottom": [
                    {
                        "shoppingcart-btn": [
                            {
                                "left": {
                                    "text": "CONTINUE Shopping"
                                }
                            },
                            {
                                "right": {
                                    "icon": "loading",
                                    "text": "UPDATE CART"
                                }
                            }
                        ]
                    },
                    {
                        "shopping-continue": {
                            "text": "Discount Codes",
                            "action": {
                                "placeholder": "Enter your coupon code",
                                "button": "APPLY COUPON"
                            }
                        }
                    },
                    {
                        "shopping-checkout": {
                            "text": "Cart Total",
                            "cart": {
                                "subtotal": "$454.98",
                                "total": "$454.98",
                                "button": "PROCEED TO CHECKOUT"
                            }
                        }
                    }
                ]
            }
        }


class Pagecheckout(Resource):
    def get(self):
        return {
            "data": {
                "text": "Check Out ",
                "url": "https://preview.colorlib.com/theme/ogani/checkout.html"
            }
        }


class Blog(Resource):
    def get(self):
        return {
            "data": {
                "text": "BLOG",
                "url": "https://preview.colorlib.com/theme/ogani/blog.html",
                "content": [
                    {
                        "banner": {
                            "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                            "text": "Blog",
                            "option": {
                                "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                "text": "Shop"
                            }
                        }
                    },
                    {
                        "blog-spad": [
                            {
                                "left": {
                                    "sidebar": [
                                        {
                                            "placeholder": "Search...",
                                            "icon": "search"
                                        },
                                        {
                                            "text": "Categories",
                                            "item": [
                                                {
                                                    "text": "All",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                },
                                                {
                                                    "text": "Beauty (20)",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                },
                                                {
                                                    "text": "Food (5)",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                },
                                                {
                                                    "text": "Life Style (9)",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                },
                                                {
                                                    "text": "Travel (10)",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Recent News",
                                            "item": [
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-1.jpg.pagespeed.ic.chNerr_ywP.webp",
                                                    "tittle": "09 Kinds Of Vegetables  Protect The Liver",
                                                    "date": "MAR 05, 2019"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-2.jpg.pagespeed.ic.NSkfePc_bi.webp",
                                                    "tittle": "Tips You To Balance Nutrition Meal Day",
                                                    "date": "MAR 05, 2019"
                                                },
                                                {
                                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-3.jpg.pagespeed.ic.IUyecbWYrU.webp",
                                                    "tittle": "4 Principles Help You Lose Weight With Vegetables",
                                                    "date": "MAR 05, 2019"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Search By",
                                            "item": [
                                                {
                                                    "text": "Apple"
                                                },
                                                {
                                                    "text": "Beauty"
                                                },
                                                {
                                                    "text": "Vegetables"
                                                },
                                                {
                                                    "text": "Fruit"
                                                },
                                                {
                                                    "text": "Healthy Food"
                                                },
                                                {
                                                    "text": "Lifestyle"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            },
                            {
                                "right": [
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                                        "blog_item_text": [
                                            {
                                                "icon": "calendar",
                                                "date": " May 4,2019"
                                            },
                                            {
                                                "icon": "comment",
                                                "value": "5"
                                            },
                                            {
                                                "text": "6 ways to prepare breakfast for 30",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                            },
                                            {
                                                "text": "READ MORE",
                                                "icon": "arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                                        "blog_item_text": [
                                            {
                                                "icon": "calendar",
                                                "date": " May 4,2019"
                                            },
                                            {
                                                "icon": "comment",
                                                "value": "5"
                                            },
                                            {
                                                "text": "Visit the clean farm in the US",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                            },
                                            {
                                                "text": "READ MORE",
                                                "icon": "arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                                        "blog_item_text": [
                                            {
                                                "icon": "calendar",
                                                "date": " May 4,2019"
                                            },
                                            {
                                                "icon": "comment",
                                                "value": "5"
                                            },
                                            {
                                                "text": "Cooking tips make cooking simple",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                            },
                                            {
                                                "text": "READ MORE",
                                                "icon": "arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                                        "blog_item_text": [
                                            {
                                                "icon": "calendar",
                                                "date": " May 4,2019"
                                            },
                                            {
                                                "icon": "comment",
                                                "value": "5"
                                            },
                                            {
                                                "text": "Cooking tips make cooking simple",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                            },
                                            {
                                                "text": "READ MORE",
                                                "icon": "arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                                        "blog_item_text": [
                                            {
                                                "icon": "calendar",
                                                "date": " May 4,2019"
                                            },
                                            {
                                                "icon": "comment",
                                                "value": "5"
                                            },
                                            {
                                                "text": "The Moment You Need To Remove Garlic From The Menu",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                            },
                                            {
                                                "text": "READ MORE",
                                                "icon": "arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-6.jpg.pagespeed.ic.P_hTD59ZOA.webp",
                                        "blog_item_text": [
                                            {
                                                "icon": "calendar",
                                                "date": " May 4,2019"
                                            },
                                            {
                                                "icon": "comment",
                                                "value": "5"
                                            },
                                            {
                                                "text": "Cooking tips make cooking simple",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                                            },
                                            {
                                                "text": "READ MORE",
                                                "icon": "arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    },
                                    {
                                        "pagination": [
                                            {
                                                "id": "1",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "id": "2",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "id": "3",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            },
                                            {
                                                "icon": "long arrow right",
                                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Blog_details(Resource):
    def get(self):
        return{
            "data": {
                "blog-dettails-spad": [
                    {
                        "left": {
                            "sidebar": [
                                {
                                    "placeholder": "Search...",
                                    "icon": "search"
                                },
                                {
                                    "text": "Categories",
                                    "item": [
                                        {
                                            "text": "All",
                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                        },
                                        {
                                            "text": "Beauty (20)",
                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                        },
                                        {
                                            "text": "Food (5)",
                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                        },
                                        {
                                            "text": "Life Style (9)",
                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                        },
                                        {
                                            "text": "Travel (10)",
                                            "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                        }
                                    ]
                                },
                                {
                                    "text": "Recent News",
                                    "item": [
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-1.jpg.pagespeed.ic.chNerr_ywP.webp",
                                            "tittle": "09 Kinds Of Vegetables  Protect The Liver",
                                            "date": "MAR 05, 2019"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-2.jpg.pagespeed.ic.NSkfePc_bi.webp",
                                            "tittle": "Tips You To Balance Nutrition Meal Day",
                                            "date": "MAR 05, 2019"
                                        },
                                        {
                                            "img": "https://preview.colorlib.com/theme/ogani/img/blog/sidebar/xsr-3.jpg.pagespeed.ic.IUyecbWYrU.webp",
                                            "tittle": "4 Principles Help You Lose Weight With Vegetables",
                                            "date": "MAR 05, 2019"
                                        }
                                    ]
                                },
                                {
                                    "text": "Search By",
                                    "item": [
                                        {
                                            "text": "Apple"
                                        },
                                        {
                                            "text": "Beauty"
                                        },
                                        {
                                            "text": "Vegetables"
                                        },
                                        {
                                            "text": "Fruit"
                                        },
                                        {
                                            "text": "Healthy Food"
                                        },
                                        {
                                            "text": "Lifestyle"
                                        }
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "right": [
                            {
                                "details-text": {
                                    "img": "https://preview.colorlib.com/theme/ogani/img/blog/…ils/xdetails-pic.jpg.pagespeed.ic.iXGi5L-xRP.webp",
                                    "text": "Sed porttitor lectus nibh. Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Vivamus magna justo,"
                                }
                            },
                            {
                                "details-content": [
                                    {
                                        "details-author": {
                                            "pic": "https://preview.colorlib.com/theme/ogani/img/blog/…/xdetails-author.jpg.pagespeed.ic.PvwPsmLHih.webp",
                                            "name": "Michael Scofield",
                                            "status": "Admin"
                                        }
                                    },
                                    {
                                        "Detail-widget": {
                                            "categories": "Food",
                                            "Tags": "All, Trending, Cooking, Healthy Food, Life Style",
                                            "sosmed": [
                                                {
                                                    "icon": "facebook",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                },
                                                {
                                                    "icon": "google plus",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                },
                                                {
                                                    "icon": "linkedin",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                },
                                                {
                                                    "icon": "email",
                                                    "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }


class Blog_postyoumaylike(Resource):
    def get(self):
        return {
            "data": {
                "text": "Post You May Like",
                "related-blog": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "6 ways to prepare breakfast for 30",
                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Visit the clean farm in the US",
                                "url": "https://preview.colorlib.com/theme/ogani/blog-details.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            }
                        ]
                    }
                ]
            }
        }


class Categories(Resource):
    def get(self):
        return {
            "data":  {
                "text": "Search By",
                "item": [
                    {
                        "text": "Apple"
                    },
                    {
                        "text": "Beauty"
                    },
                    {
                        "text": "Vegetables"
                    },
                    {
                        "text": "Fruit"
                    },
                    {
                        "text": "Healthy Food"
                    },
                    {
                        "text": "Lifestyle"
                    }
                ]
            }
        }


class Recent_News(Resource):
    def get(self):
        return {
            "data": {
                "right": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "6 ways to prepare breakfast for 30",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Visit the clean farm in the US",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "The Moment You Need To Remove Garlic From The Menu",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-6.jpg.pagespeed.ic.P_hTD59ZOA.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "pagination": [
                            {
                                "id": "1",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "id": "2",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "id": "3",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "icon": "long arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    }
                ]
            }
        }


class Conten(Resource):
    def get(Self):
        return {
            "data": {
                "konten": [
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-2.jpg.pagespeed.ic.Wv9OXwE7iA.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "6 ways to prepare breakfast for 30",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-3.jpg.pagespeed.ic.ruf-U0Iaxk.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Visit the clean farm in the US",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-1.jpg.pagespeed.ic.b6c8D8etPg.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-4.jpg.pagespeed.ic.LvzO2aM5LQ.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "The Moment You Need To Remove Garlic From The Menu",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "img": "https://preview.colorlib.com/theme/ogani/img/blog/xblog-6.jpg.pagespeed.ic.P_hTD59ZOA.webp",
                        "blog_item_text": [
                            {
                                "icon": "calendar",
                                "date": " May 4,2019"
                            },
                            {
                                "icon": "comment",
                                "value": "5"
                            },
                            {
                                "text": "Cooking tips make cooking simple",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "text": "Sed quia non numquam modi tempora indunt ut labore et dolore magnam aliquam quaerat"
                            },
                            {
                                "text": "READ MORE",
                                "icon": "arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    },
                    {
                        "pagination": [
                            {
                                "id": "1",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "id": "2",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "id": "3",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            },
                            {
                                "icon": "long arrow right",
                                "url": "https://preview.colorlib.com/theme/ogani/blog.html#"
                            }
                        ]
                    }
                ]
            }
        }


class Contac(Resource):
    def get(self):
        return {
            "data": {
                "text": "CONTACT",
                "url": "https://preview.colorlib.com/theme/ogani/contact.html",
                "contact": [
                    {
                        "banner": {
                            "img": "https://preview.colorlib.com/theme/ogani/img/breadcrumb.jpg",
                            "text": "Contact Us",
                            "option": {
                                "Home": "https://preview.colorlib.com/theme/ogani/index.html",
                                "text": "Contact Us"
                            }
                        }
                    },
                    {
                        "conatct-spad": [
                            {
                                "icon": "phone",
                                "text": "Phone",
                                "tell": "+01-3-8888-6868"
                            },
                            {
                                "icon": "pin",
                                "text": "Address",
                                "tell": "60-49 Road 11378 New York"
                            },
                            {
                                "icon": "clock",
                                "text": "Open Time",
                                "tell": "10:00 am to 23:00 pm"
                            },
                            {
                                "icon": "mail",
                                "text": "Email",
                                "tell": "hello@colorlib.com"
                            }
                        ]
                    },
                    {
                        "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d49116.39176087041!2d-86.41867791216099!3d39.69977417971648!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x886ca48c841038a1%3A0x70cfba96bf847f0!2sPlainfield%2C%20IN%2C%20USA!5e0!3m2!1sen!2sbd!4v1586106673811!5m2!1sen!2sbd",
                        "map-inside": {
                            "icon": "pin",
                            "City": "New York",
                            "Phone": "+12-345-6789",
                            "address": "16 Creek Ave. Farmingdale, NY"
                        }
                    },
                    {
                        "text": "Leave Message",
                        "form": [
                            {
                                "placeholder": "Your Name"
                            },
                            {
                                "placeholder": "Your Email"
                            },
                            {
                                "placeholder": "Your Message"
                            },
                            {
                                "button":  "SEND MESSAGE"
                            }
                        ]
                    }
                ]
            }
        }


api.add_resource(Home, '/home/')
api.add_resource(Slider, '/home/slider/')
api.add_resource(Lates_products, '/home/lates_products/')
api.add_resource(Toprateds_products, '/home/toprateds_products/')
api.add_resource(Review_products, '/home/review_products/')
api.add_resource(Feuturedspad, '/home/feuturedproduct/')
api.add_resource(Container, '/home/container/')
api.add_resource(Menublog_spand, '/home/fromtheblog/')
api.add_resource(Shop, '/shop/')
api.add_resource(Productspad, '/shop/productspad/')
api.add_resource(Shop_departemint, '/shop/departement')
api.add_resource(Shop_price, '/shop/price/')
api.add_resource(Shop_color, '/shop/color/')
api.add_resource(Shop_size, '/shop/size/')
api.add_resource(ShopLates_products, '/Shop/latesproducts/')
api.add_resource(Shoproduts_discount, '/shop/productsdiscount/')
api.add_resource(Shopfilter_item, '/shop/filterproduct/')
api.add_resource(Shopproduct, '/shop/product/')
api.add_resource(Pages, '/pages/')
api.add_resource(Pagesproduct_detail, '/page/productdetail/')
api.add_resource(Pagesrelated_product, '/page/relatedproduct/')
api.add_resource(Pageshoping_chart, '/page/shopchart/')
api.add_resource(Pagecheckout, '/page/checkout/')
api.add_resource(Blog, '/blog/')
api.add_resource(Blog_details, '/blog/details/')
api.add_resource(Blog_postyoumaylike, '/blog/postoumaylike/')
api.add_resource(Categories, '/blog/categories/')
api.add_resource(Recent_News, '/blog/recent_news/')
api.add_resource(Conten, '/blog/conten/')
api.add_resource(Contac, '/contac/')


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "not found end point"}, 404


if __name__ == '__main__':
    app.run(debug=True)
