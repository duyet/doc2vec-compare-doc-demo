
var app = angular.module('duyet', []);
app.controller('controller', function ($scope, $http) {
	$scope.compare = function() {
		$scope.compare_result = null;

		var doc1 = $('#contentInput1').val();
		var doc2 = $('#contentInput2').val();

		if (!doc1 || !doc2) return alert("Please select an input.")

		var data = { doc1: doc1, doc2: doc2 };

		$http.post('/api/compare_2', data).then(function(response) {
			$scope.compare_result = response.data;
		}, function(response) {
			alert('Something went wrong');
		})
	}
})
