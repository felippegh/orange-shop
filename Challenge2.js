const inquirer = require('inquirer')

var questions = [
  {
    type: 'input',
    name: 'number_containers',
    message: "Please, insert number of containers:"
  },
  {
    type: 'input',
    name: 'fruits_container',
    message: "Please, insert the number of fruits per container:"
  },
  {
    type: 'input',
    name: 'fruit_price',
    message: "Please, insert orange price:"
  },
]

inquirer.prompt(questions).then(answers => {
  let number_containers = answers['number_containers'];
  let fruits_container = answers['fruits_container'];
  let fruit_price = answers['fruit_price'];
  let balance = 0;
  let oranges_available = number_containers * fruits_container;
  let apples_available = 0;


  let mainMenu = function () {
    console.log(`\nORANGE SHOP MENU\n1 - Sell Apples \n2 - Sell Oranges\n3 - Show current balance\n4 - Exit program`);
    inquirer.prompt({
      type: 'input',
      name: 'menu_option',
      message: "Please, choose your option:"
    }).then(answers => {
      let menu_option = answers['menu_option'];

      switch (menu_option) {
        case '1':
          inquirer.prompt({
            type: 'input',
            name: 'apples_to_sell',
            message: `How many apples do you want to sell? You currently have ${apples_available} apples.`
          }).then(answers => {
            let apples_to_sell = parseInt(answers['apples_to_sell']);
          
            if (apples_to_sell > apples_available) {
              console.log(`You don't have enough apples :(`);
              mainMenu();
            }
            apples_available -= apples_to_sell;
            balance += apples_to_sell * fruit_price;
            mainMenu();
          })
          break;

        case '2':
          inquirer.prompt({
            type: 'input',
            name: 'oranges_to_sell',
            message: `How many oranges do you want to sell? You currently have ${oranges_available} oranges.`
          }).then(answers => {
            let oranges_to_sell = parseInt(answers['oranges_to_sell']);
          
            if (oranges_to_sell > oranges_available) {
              console.log(`You don't have enough oranges :(`);
              mainMenu();
            }
            oranges_available -= oranges_to_sell;
            balance += oranges_to_sell * fruit_price;
            mainMenu();
          })
          break;

        case '3':
          console.log(`Current balance: ${balance} dollars`);
          break;

        case '4':
          process.exit();

        default:
          console.log('Option invalid, please try again!');

      }

      mainMenu();
    })
  }

  mainMenu();

  // console.log(`Number of containers: ${answers['number_containers']} \n Fruits per container: ${answers['fruits_container']} \n Orange price: ${answers['fruit_price']}`)
})

