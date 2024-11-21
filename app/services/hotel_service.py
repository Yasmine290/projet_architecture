from services.api_site1 import ApiSite1
# from services.api_site2 import ApiSite2
class HotelService:
    def __init__(self):
        self.api_clients = [ApiSite1()]

    def compare_prices(self, destination, check_in, check_out, guests):
        results = []
        for client in self.api_clients:
            try:
                site_results = client.get_hotel_prices(destination, check_in, check_out, guests)
                results.extend(site_results)
            except Exception as e:
                print(f"Error with {client.__class__.__name__}: {e}")
        return sorted(results, key=lambda x: x['price'])
