from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User, Match, Participants, UserMatch
from .SearchForm import SearchForm
from search.src import getData
from django.utils import timezone


def test(request):
    return HttpResponse("하이요")


def index(request):
    user_list = User.objects.order_by("-updateDate")
    context = {"user_list": user_list}
    return render(request, 'index.html', context)


def searchCreate(request):
    form = SearchForm()
    return render(request, 'searchForm.html', {'form': form})


def updateUser(request, userName):
    data = getData.getDataByName(userName)
    user = User(userName=userName, tear="챌린저", updateDate=timezone.now(), summonerLevel=data['summonerLevel'])
    context = {"user": user}
    return render(request, "userDetail.html", context)


def test(request):
    data = getData.getMatch("우리팀이 짱이야", 100)
    matches = []
    for d in data:
        match = UserMatch()
        match.platformId = d['platformId']
        match.gameId = d['gameId']
        match.champion = d['champion']
        match.season = d['season']
        match.timestamp = d['timestamp']
        match.role = d['role']
        matches.append(match)
    context = {'matches': matches}
    return render(request, "test.html", context)


def test2(request):
    user = f()
    data = getData.getMatch("우리팀이 짱이야", 100)
    matches = []
    for d in data:
        match = UserMatch()
        match.userName = user
        match.platformId = d['platformId']
        match.gameId = d['gameId']
        match.champion = d['champion']
        match.season = d['season']
        match.timestamp = d['timestamp']
        match.role = d['role']
        matches.append(match)
    context = {'matches': matches, 'user': user}
    return render(request, "test2.html", context)


def f(userName="우리팀이 짱이야"):
    iconImg = '/'
    try:
        user = User.objects.get(userName=userName)
        iconImg = "/static/img/profileIcon/" + str(user.profileIconId) + '.png'
    except:
        try:
            data = getData.getDataByName(userName)
            playerInfo = getData.getPlayerInfo(userName)
            user = User(userName=data['name'], updateDate=timezone.now())
            for info in playerInfo:
                if info['queueType'] == 'RANKED_SOLO_5x5':
                    user.soloTier = info['tier'] + ' ' + info['rank']
                    user.soloWins = info['wins']
                    user.soloLosses = info['losses']
                    user.soloLeaguePoint = info['leaguePoints']
                elif info['queueType'] == 'RANKED_FLEX_SR':
                    user.flexTier = info['tier'] + ' ' + info['rank']
                    user.flexWins = info['wins']
                    user.flexLosses = info['losses']
                    user.flexLeaguePoint = info['leaguePoints']
            user.summonerLevel = data['summonerLevel']
            user.profileIconId = data['profileIconId']
            iconImg = "/static/img/profileIcon/" + str(user.profileIconId) + '.png'
        except:
            user = None
    return user


def searchUser(request):
    if request.method == 'POST':
        userName = request.POST['userName']
    iconImg = '/'
    try:
        user = User.objects.get(userName=userName)
        iconImg = "/static/img/profileIcon/" + str(user.profileIconId) + '.png'
    except:
        try:
            data = getData.getDataByName(userName)
            playerInfo = getData.getPlayerInfo(userName)
            user = User(userName=userName, updateDate=timezone.now())
            for info in playerInfo:
                if info['queueType'] == 'RANKED_SOLO_5x5':
                    user.soloTier = info['tier'] + ' ' + info['rank']
                    user.soloWins = info['wins']
                    user.soloLosses = info['losses']
                    user.soloLeaguePoint = info['leaguePoints']
                elif info['queueType'] == 'RANKED_FLEX_SR':
                    user.flexTier = info['tier'] + ' ' + info['rank']
                    user.flexWins = info['wins']
                    user.flexLosses = info['losses']
                    user.flexLeaguePoint = info['leaguePoints']
            user.summonerLevel = data['summonerLevel']
            user.profileIconId = data['profileIconId']
            iconImg = "/static/img/profileIcon/" + str(user.profileIconId) + '.png'
        except:
            user = None
    context = {'user': user, 'iconImg': iconImg}
    return render(request, 'userDetail.html', context)
