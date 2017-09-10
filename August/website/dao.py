# Create interface to access to database
from models import order, type, product, user

def get_9_best_seller():
	result = product.objects.order_by('ordered_number').all()[:9]
	return result

def get_product(type_id):
	result = product.objects.filter(type_id =type_id)
	return result
