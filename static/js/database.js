function ShowDashboard() {
    document.getElementById('dashboard').style.display = 'block';
    document.getElementById('user').style.display = 'none';
    document.getElementById('healthgoal').style.display = 'none';
    document.getElementById('workouts').style.display = 'none';
    document.getElementById('mealsplans').style.display = 'none';
    document.getElementById('progresstracker').style.display = 'none';
}

function ShowUsers() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'block';
    document.getElementById('healthgoal').style.display = 'none';
    document.getElementById('workouts').style.display = 'none';
    document.getElementById('mealsplans').style.display = 'none';
    document.getElementById('progresstracker').style.display = 'none';
}

function ShowHealthGoal() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('healthgoal').style.display = 'block';
    document.getElementById('workouts').style.display = 'none';
    document.getElementById('mealsplans').style.display = 'none';
    document.getElementById('progresstracker').style.display = 'none';
}

function ShowWorkOuts() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('healthgoal').style.display = 'none';
    document.getElementById('workouts').style.display = 'block';
    document.getElementById('mealsplans').style.display = 'none';
    document.getElementById('progresstracker').style.display = 'none';
}

function ShowMealsPlans() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('healthgoal').style.display = 'none';
    document.getElementById('workouts').style.display = 'none';
    document.getElementById('mealsplans').style.display = 'block';
    document.getElementById('progresstracker').style.display = 'none';
}

function ShowProgressTracker() {
    document.getElementById('dashboard').style.display = 'none';
    document.getElementById('user').style.display = 'none';
    document.getElementById('healthgoal').style.display = 'none';
    document.getElementById('workouts').style.display = 'none';
    document.getElementById('mealsplans').style.display = 'none';
    document.getElementById('progresstracker').style.display = 'block';
}

function showSection(section) {
    document.querySelectorAll('.content-section').forEach(function(sec) {
        sec.style.display = 'none';
    });
    document.getElementById(section).style.display = 'block';
}

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const section = urlParams.get('section');
    if (section) {
        showSection(section);
    } else {
        showSection('dashboard');
    }
};