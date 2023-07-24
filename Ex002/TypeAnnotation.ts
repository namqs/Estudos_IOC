// Variáveis
let nome: string = 'Natalie Marques';
console.log(nome);

//array
let animais: string[] = ['Cachorro', 'Gato', 'Canguru', 'Capivara'];
console.log(animais);

//objetos
let carro: {
  nome:string;
  ano: number;
  preço: number;
};

carro = {nome: 'Toyota', ano: 2019, preço: 50.000};
console.log(carro);

//função
function multiplicarNumero (num1: number, num2: number)
{
  return num1 * num2;
}
console.log(multiplicarNumero(2,5));