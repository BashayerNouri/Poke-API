from django.shortcuts import render
import requests


# {
# 	"count": 365,
# 	"next": "http://pokeapi.co/api/v2/evolution-chain/?limit=20&offset=20",
# 	"previous": null,
# 	"results": [{
# 		"url": "http://pokeapi.co/api/v2/evolution-chain/1/"
# 	}]
# }
#
# https://github.com/PokeAPI/pokeapi/blob/master/pokemon_v2/README.md#abilities
#
#


# Create your views here.

def pokemon_list(request):
	url = "https://pokeapi.co/api/v2/pokemon/"
	pre = request.GET.get('pre')
	nxt = request.GET.get('nxt')

	if nxt:
		response = requests.get(nxt).json()
	elif pre: 
		response = requests.get(pre).json()
	else:
		response = requests.get(url).json()
		
	context = {
	"responses": response,
	}
	return render(request,'pokemon_list.html',context)


def pokemon_detail(request):
	url = request.GET.get('detail')
	response = requests.get(url).json()

	context = {
	"response": response,
	}
	return render(request,'pokemon_detail.html',context)