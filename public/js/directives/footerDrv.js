(function () {
    angular.module('myApp').directive('footerDrv', [function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/footerDrv.html',
            replace: true,
            scope: {
                categories: '='
            }
        };
    }]);
})();
