(function () {
    'use strict';
    
    angular.module('booking.demo')
        .directive('bookingSeat', SeatDirective);
        
    function SeatDirective(){
        return {
            templateUrl: '/static/html/card.html',
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http) {
                var url = '/booking/seats/' + $scope.card.id + '/';
                $scope.destList = $scope.list;
                
                $scope.update = function () {
                    return $http.put(
                        url,
                        $scope.card
                    );
                };
                
                function removeCardFromList(card, list) {
                    var cards = list.cards;
                    cards.splice(
                        cards.indexOf(card),
                        1
                        );
                }
                
                $scope.delete = function () {
                    $http.delete(url).then(
                        function () {
                            removeCardFromList($scope.card, $scope.list);
                        }
                    );
                };
                
                $scope.modelOptions = {
                    debounce: 500
                };
                
                $scope.move = function () {
                    if ($scope.destList === undefined) {
                        return;
                    }
                    $scope.card.list = $scope.destList.id;
                    console.log($scope.card.list);
                    $scope.update().then(function () {
                        {
                            removeCardFromList($scope.card, $scope.list);
                            $scope.destList.cards.push($scope.card);
                        }
                    });
                };
                
            }]
        };
    }
    
})();
