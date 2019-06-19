from django.shortcuts import render

# Create your views here.

def index (request):
	tweets = NewTweet.objects.values_list('tweet',flat=True)
	f = {
	    'tweets':tweets,
	}
	return render(request,'index/index.html',f)


def new(request):
	#forms.pyで定義されて表示される新規ツイートフォームで（メソッドはPOST）入力された内容をnew_tweet変数に代入
    new_tweet = NewTweetForm(request.POST or None)
    if new_tweet.is_valid():
    	#cleane_data バリデーションに通ったデータを整形して返り値として返す関数
        new_tweet = new_tweet.cleaned_data
        new_tweet = new_tweet['tweet']
        tweet = NewTweet(tweet=new_tweet)
        #入力内容の保存
        tweet.save()
        #topページにリダイレクトリダイレクト（indexアクションに飛ぶ）
        return redirect('/')
    else:
        new_tweet = new_tweet.as_table()
        f = {
            'new_tweet': new_tweet,
            }
        return render(request, 'index/new.html', f)
#tweet_idを引数として受け取っている。
def delete(request, tweet_id):
    NewTweet.objects.filter(id=tweet_id).delete()
    return redirect('/')

#tweetの更新
def update(request,tweet_id):
	new_tweet = NewTweetForm(request.POST or None)
	#入力欄が空白でないか等のチェック
	if new_tweet.is_valid():
		new_tweet = new_tweet.cleaned_data['tweet']
		old_tweet = NewTweet.objects.get(id=tweet_id)
		old_tweet.tweet = new_tweet
		old_tweet.save()
		return redirect('/')
    else:
    	new_tweet = new_tweet.as_table()
    	f={
    	  'new_tweet':new_tweet,
    	  }
    	 return render(request,'index/update.html',f)




