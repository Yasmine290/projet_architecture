class BaseProduct:
    def get_prices(self, **kwargs):
        raise NotImplementedError("Subclasses must implement get_prices.")
