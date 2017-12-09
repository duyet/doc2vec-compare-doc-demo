var app = angular.module('duyet', []);

app.controller('controller', function ($scope, $http) {
	$scope.list_data = [];
	$scope.file_content = null

	$http.get('/api/data/list').then(function(response) {
		$scope.list_data = response.data;
	}, function() {
		alert('Something went wrong!');
	});

	$scope.load_file = function (filename) {
		$scope.file_content = null;
		$http.get('/api/data/' + filename).then(function(response) {
			$scope.file_content = response.data;
		}, function() {
			alert('Something went wrong!');
		});

	}
})
