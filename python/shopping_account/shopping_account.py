# shopping account


class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


# ---
# product = Product("Apple", 200)
# print(f"{product.name}: {product.price}")
# ---


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity


# ---
# cart_item = CartItem(product, 5)
# print(
#     f"{cart_item.product.name}:",
#     f"{cart_item.product.price} *",
#     f"{cart_item.quantity}",
# )
# ---


class Coupon:
    def __init__(self, product_name: str, discount: float):
        self.product_name = product_name
        self.discount = discount


# ---
# coupon = Coupon("Apple", 0.1)  # 10% off
# print(f"{coupon.product_name}, 値引き割合:{coupon.discount}")
# ---


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, cart_item: CartItem):
        self.items.append(cart_item)

    def remove_item(self, cart_item: CartItem):
        if cart_item in self.items:
            self.items.remove(cart_item)


# ---
# カートに入れる商品
# cart_apple = CartItem(Product("Apple", 200), 5)
# cart_banana = CartItem(Product("Banana", 100), 3)
# cart_orange = CartItem(Product("Orange", 150), 4)
# ショッピングカートをインスタンス
# cart = ShoppingCart()
# カートに商品を追加
# cart.add_item(cart_apple)
# cart.add_item(cart_banana)
# cart.add_item(cart_orange)
# カートの商品を削除
# cart.remove_item(cart_banana)
# ---


class Account:
    def __init__(self, name: str):
        self.name = name
        self.coupons = {}
        self.cart = ShoppingCart()

    def add_coupon(self, coupon: Coupon):
        self.coupons[coupon.product_name] = coupon

    def show_items_with_coupons(self):
        print("Show cart items")

        if len(self.cart.items) <= 0:
            print("nothing")
            return

        for cart_item in self.cart.items:
            print(
                f"{cart_item.product.name}:",
                f"¥{cart_item.product.price} *",
                f"{cart_item.quantity}",
            )
            coupon = self.coupons.get(cart_item.product.name)
            if coupon:
                print(
                    f"  Coupon: {coupon.product_name},",
                    f"{coupon.discount * 100}% off",
                )

        print()

    def calculate_total(self):
        total = 0
        for cart_item in self.cart.items:
            item_price = cart_item.product.price
            coupon = self.coupons.get(cart_item.product.name)
            if coupon:
                item_price *= 1 - coupon.discount
            total += item_price * cart_item.quantity
        return total

    def show_checkout_summary(self):
        print("\nCheckout")
        print("---------")
        self.show_items_with_coupons()
        total = self.calculate_total()
        print(f"Total: ¥{total}")
        print("---------\n")


# アカウントを作成
account = Account("John Doe")

# カートに入れる商品
cart_apple = CartItem(Product("Apple", 200), 5)
cart_banana = CartItem(Product("Banana", 100), 3)
cart_orange = CartItem(Product("Orange", 150), 4)

# クーポンを追加
account.add_coupon(Coupon("Apple", 0.1))  # Apple 10% off
account.add_coupon(Coupon("Orange", 0.2))  # Orange 20% off

# チェックアウト（会計表示）
account.show_checkout_summary()

# +++

# 商品をカートに入れる
account.cart.add_item(cart_apple)
account.cart.add_item(cart_banana)
account.cart.add_item(cart_orange)

account.show_checkout_summary()

# +++

# 商品をカートから出す
account.cart.remove_item(cart_apple)

account.show_checkout_summary()
