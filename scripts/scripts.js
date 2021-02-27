/* CÓDIGO PARA CÁLCULO DE ELO */
var ngApp = angular.module('myNgApp', []);

ngApp.controller('myController', function ($scope) {
    $scope.elo = 0;

    $scope.calcular_elo=function(elo, elo_rivales, resultados){

        $scope.elo_rival = 0;
        $scope.exp = 0;
        $scope.factor = 0;
        $scope.variacion = 0;
        var resultado = 0;
            
        if($scope.elo > 2200){
            factor = 10;
        }
        else{
            if($scope.elo>2000){
                factor = 15;
            }
            else{
                if($scope.elo>1800){
                    factor = 20;
                }
                else{
                    if($scope.elo>1600){
                        factor = 25;
                    }
                    else{
                        factor = 30;
                    }
                }
            }
        }


        elo_rivales.forEach(calcular_expectativa);

        function calcular_expectativa(elemento){
            if(elemento >= 1000){
                $scope.exp = $scope.exp + (1 / (1 + Math.pow(10, ((elemento - elo)/400))));
            }
        }
        resultados.forEach(sumar_resultados);

        function sumar_resultados(elemento){
            if(elemento === "0.5"){
                elemento = 0.5;
            }
            else{
                elemento = parseInt(elemento, 10);
            }
            if(elemento >= 0){
                resultado += elemento;
            }
        }

        console.log("Resultado: " + resultado - $scope.exp);

        $scope.variacion = resultado - $scope.exp;
        $scope.variacion = $scope.variacion * factor;
        $scope.variacion = $scope.variacion.toFixed(2);

        if($scope.variacion >= 0){
            document.getElementById("tendencia").src="img/arriba.png";            
        }
        else{
            document.getElementById("tendencia").src="img/abajo.png";
        }

        $scope.variacion = Math.abs($scope.variacion);
    };

});

/* CÓDIGO PARA EL TABLERO */