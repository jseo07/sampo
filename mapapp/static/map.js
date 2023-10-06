var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
            mapOption = { 
                center: new kakao.maps.LatLng(36.491572371796956, 127.25705099733301), // 지도의 중심좌표
                level: 6 // 지도의 확대 레벨
            };

// 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
var map = new kakao.maps.Map(mapContainer, mapOption); 

var geocoder = new kakao.maps.services.Geocoder();

// 지도를 클릭한 위치에 표출할 마커입니다
var marker = new kakao.maps.Marker({ 
    // 지도 중심좌표에 마커를 생성합니다 
    position: map.getCenter() 
});

var geocoder = new kakao.maps.services.Geocoder();

// 지도에 클릭 이벤트를 등록합니다
// 지도를 클릭하면 마지막 파라미터로 넘어온 함수를 호출합니다
kakao.maps.event.addListener(map, 'click', function(mouseEvent) {        
    
    // 클릭한 위도, 경도 정보를 가져옵니다 
    var latlng = mouseEvent.latLng; 
    var lat = latlng.getLat();
    var lng = latlng.getLng();

    searchDetailAddrFromCoords(mouseEvent.latLng, function(result, status) {
        if (status === kakao.maps.services.Status.OK) {
            var detailAddr = !!result[0].road_address ? '도로명주소 : ' + result[0].road_address.address_name: '';
            detailAddr += ' 지번 주소 : ' + result[0].address.address_name;
            var content = detailAddr;

            document.getElementById("address").value = content;

        }   
    });
    
    
    // 마커 위치를 클릭한 위치로 옮깁니다
    marker.setPosition(latlng);

    var message = '클릭한 위치의 위도는 ' + lat + ' 이고, ';
    message += '경도는 ' + lng + ' 입니다';

    var resultDiv = document.getElementById('clickLatlng'); 
    resultDiv.innerHTML = message;

    // 지도에 마커를 표시합니다
    marker.setMap(map);

    function searchDetailAddrFromCoords(coords, callback) {
        // 좌표로 법정동 상세 주소 정보를 요청합니다
        geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
    }

});