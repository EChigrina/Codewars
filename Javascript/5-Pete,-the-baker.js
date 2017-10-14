function cakes(recipe, available) {
  var x = [];
  for (var prop in recipe) {
    if (available.hasOwnProperty(prop)) {
		x[x.length] = Math.floor(available[prop]/recipe[prop]);        
    }
	else {
		return 0;
	}
  }
  return Math.min.apply(Math,x);
}
