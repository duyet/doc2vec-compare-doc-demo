
var app = angular.module('duyet', []);
app.controller('controller', function ($scope, $http) {
	$scope.compare = function() {
		$scope.compare_result = null;

		var doc1 = $('#contentInput1').val();

		if (!doc1) return alert("Please select an input.")

		var data = { doc: doc1 };

		$http.post('/api/compare_all', data).then(function(response) {
			$scope.compare_result = response.data;
		}, function(response) {
			alert('Something went wrong');
		})
	}

	$scope.load_file = function (filename) {
		$scope.file_content = null;
		$http.get('/api/data/' + filename).then(function(response) {
			$scope.file_content = response.data;
		}, function() {
			alert('Something went wrong!');
		});

	}
})
