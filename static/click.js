
const foods = document.querySelectorAll('food');
foods.addEventListener('click')

query.selector('food')
  .addEventListener('click', clickedFood)
//something happens when you click food//

  .function clickedFood() {
    console.log('You clicked food');
  }

function clickedFood(e)
//(e) means event
{
  console.log('You clicked food');
  console.log(e);
  // when you click food, in the console it will state 'You clicked food'//
}

function clickedFood(e) {
  console.log('You clicked ' + e.target.innertText.);
  if (food == 'Burgers') {
    document.querySelector('#header'). innertText = 'The ingredients for ' + food_in;
    document.querySelector('#ingredients'). innertText = 'ingredients';
    //this is used to put 'meat, buns' to describe the 'ingredients' for the Burger.//
  }
}
food.addEventListener('mouseout', (e)

clickedElement.style.fontWeight = 'bold';
