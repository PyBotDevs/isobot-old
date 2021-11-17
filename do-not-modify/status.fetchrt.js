console.log('FetchRT successfully initilazed.')
elementLabel = ''
elementContainer = ''
function initilaze(status, elementContainer, elementLabel) {
    if(status=='offline') {
        displayOffline()
        console.log('Status set to \'offline\'.')
    }
    else if(status=='online') {
        displayOnline()
        console.log('Status set to \'online\'.')
    }
    else if(status=='repair') {
        displayRepair()
        console.log('Status set to \'repair\'.')
    }
    else if(status=='critical') {
        displayCritical()
        console.log('Status set to \'critical\'.')
    }
    else {
        displayOffline()
        console.error(status + ' is not a valid status. Default status has been set to \'offline\'')
    }
}
function displayOffline() {
    document.getElementById(elementContainer).style.backgroundColor = rgb(24, 24, 24);
    document.getElementById(elementLabel).innerHTML = 'Offline';
}
function displayOnline() {
    document.getElementById(elementContainer).style.backgroundColor = 'green';
    document.getElementById(elementLabel).innerHTML = 'Online';
}
function displayRepair() {
    document.getElementById(elementContainer).style.backgroundColor = 'orange';
    document.getElementById(elementLabel).innerHTML = 'Under Maintainance';
}
function displayCritical() {
    document.getElementById(elementContainer).style.backgroundColor = 'red';
    document.getElementById(elementLabel).innerHTML = 'Critical Issue (Under Maintainance)';
}
