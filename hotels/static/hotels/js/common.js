/**
 * Created with JetBrains WebStorm.
 * User: 黄辉泉
 * Date: 13-5-29
 * Time: 下午10:05
 * To change this template use File | Settings | File Templates.
 */
window.onload = function(){
    var roomTotalHandle = document.getElementById("roomTotal");
    if(roomTotalHandle){
        roomTotalHandle.onchange = function(){
            var total = roomTotalHandle.value;
            var tableHandle = document.getElementById("ChooseRoomType").getElementsByTagName("table")[0];
            var firstTr = tableHandle.getElementsByTagName("tr")[0];
            while(tableHandle.hasChildNodes()){
                tableHandle.removeChild(tableHandle.firstChild);
            }
            tableHandle.appendChild(firstTr);
            for(var i = 0; i < total - 1; i++){
                var tr = document.createElement("tr");
                tr.innerHTML = '<td></td><td>Room ' + (i+2) + '</td><td>Adults<input type="number" name="room_' + (i+2) + '_adults"/></td><td>Children <input type="number" name="room_' + (i+2) + '_children"/></td>';
                tableHandle.appendChild(tr);
            }
        }
    }
    var submitRoomTypeHandle = document.getElementById("submitRoomType");
    if(submitRoomTypeHandle){
        submitRoomTypeHandle.onclick = function(e){
            var submitHandle = document.getElementById("submit");
            submitHandle.click();
            e.preventDefault();
        }
    }

    var  virtualHandle = document.getElementById("virtual");
    if(virtualHandle){
        var submitHandle = document.getElementById("submit");
        var continueHandle = document.getElementsByClassName("continue");
        for (var i = continueHandle.length - 1; i >= 0; i--) {
            continueHandle[i].onclick = function(e){
                var hotelId = this.getAttribute("data-hotelId");
                virtualHandle.setAttribute("action","../"+ hotelId + "/checkRoom/");
                submitHandle.click();
                e.preventDefault();
            }
        };
        
    }

    var  virtualHandle_ano = document.getElementById("virtual_ano");
    if(virtualHandle_ano){
        var submitHandle = document.getElementById("submit");
        var continueHandle = document.getElementsByClassName("continue");
        for (var i = continueHandle.length - 1; i >= 0; i--) {
            continueHandle[i].onclick = function(e){
                var cityHandle = document.getElementById("city");
                cityHandle.value = this.innerHTML;
                submitHandle.click();
                e.preventDefault();
            }
        };
        
    }

    var backHandle = document.getElementById("back");
    if(backHandle){
        backHandle.onclick = function(e){
            window.history.back();
            e.preventDefault();
        }
    }
    var inputHandle = document.getElementsByTagName("input");
    for (var i = inputHandle.length - 1; i >= 0; i--) {
        inputHandle[i].setAttribute("required", "required");
    };
}
