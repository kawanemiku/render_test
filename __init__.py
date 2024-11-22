from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    # 1 人の時は"None"と記述します．
    NUM_ROUNDS = 1
    # 1 回だけ質問します．


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender=models.CharField(initial=None,choices=['男性','女性','その他'],verbose_name='あなたの性別を教えてください。',widget=widgets.RadioSelect)
    #ラジオボタンを使うときには"widget"で設定できる
    q_age=models.IntegerField(verbose_name='あなたの年齢を教えてください。',choices=range(0,125),initial=None)
    #数字の場合は"choices"を使うことで範囲を指定
    q_area=models.CharField(initial=None,choices=['北海道','青森県','岩手県','宮城県','秋田県','山形県','福島県','茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県','山梨県','長野県','新潟県','富山県','石川県','福井県','岐阜県','静岡県','愛知県','三重県','滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県','鳥取県','島根県','岡山県','広島県','山口県','徳島県','香川県','愛媛県','高知県','福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県'],verbose_name='あなたのお住まいの都道府県を教えてください。')
    q_image=models.CharField(initial=None,choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'],verbose_name='あなたの大阪に対するイメージを教えてください。')
    q_hukei=models.CharField(initial=None,choices=['道頓堀（グリコの看板）','大阪城','通天閣','USJ','自然風景','大阪駅周辺・高層ビル街','太陽の塔・万博記念公園','海遊館','関西空港','天王寺公園','古墳'],verbose_name='大阪といえばどの風景（場所）を思い浮かべますか。')
    q_hukeiimage=models.CharField(initial=None,choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'],verbose_name='上の質問で答えた場所についてのイメージを教えてください。')
    q_yosa=models.CharField(initial=None,choices=['はい','いいえ','きれい'],verbose_name='上の質問でとても汚いと思うまたは汚いと思うと答えた人にお聞きします。汚いことがその場所の良さでもあると思いますか。(わからない、きれいだと思う、とてもきれいだと思うと答えた人は「きれい」にチェックを入れてください。)',widget=widgets.RadioSelect)
    comment=models.StringField(initial=None,verbose_name='場所のイメージについての質問においてきれい、汚いと思った理由を教えてください。')
    image1=models.StringField(initial=None,verbose_name='下の写真のイメージについて教えてください。',choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'])
    know1=models.CharField(initial=None,verbose_name='上の写真の風景が大阪にあることを知っていますか。',choices=['はい','いいえ'],widget=widgets.RadioSelect)
    image2=models.StringField(initial=None,verbose_name='下の写真のイメージについて教えてください。',choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'])
    know2=models.CharField(initial=None,verbose_name='上の写真の風景が大阪にあることを知っていますか。',choices=['はい','いいえ'],widget=widgets.RadioSelect)
    image3=models.StringField(initial=None,verbose_name='下の写真のイメージについて教えてください。',choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'])
    know3=models.CharField(initial=None,verbose_name='上の写真の風景が大阪にあることを知っていますか。',choices=['はい','いいえ'],widget=widgets.RadioSelect)
    image4=models.StringField(initial=None,verbose_name='下の写真のイメージについて教えてください。',choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'])
    know4=models.CharField(initial=None,verbose_name='上の写真の風景が大阪にあることを知っていますか。',choices=['はい','いいえ'],widget=widgets.RadioSelect)
    image5=models.StringField(initial=None,verbose_name='下の写真のイメージについて教えてください。',choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'])
    know5=models.CharField(initial=None,verbose_name='上の写真の風景が大阪にあることを知っていますか。',choices=['はい','いいえ'],widget=widgets.RadioSelect)
    image6=models.StringField(initial=None,verbose_name='下の写真のイメージについて教えてください。',choices=['とてもきれいだと思う','きれいだと思う','わからない','汚いと思う','とても汚いと思う'])
    know6=models.CharField(initial=None,verbose_name='上の写真の風景が大阪にあることを知っていますか。',choices=['はい','いいえ'],widget=widgets.RadioSelect)

class Page1(Page):
    form_model='player'
    form_fields=['q_image','q_hukei','q_hukeiimage','q_yosa','comment']

class Page2(Page):
    form_model='player'
    form_fields=['image1','know1','image2','know2','image3','know3','image4','know4','image5','know5','image6','know6']
    
class Page3(Page):
    form_model='player'
    form_fields=['q_gender','q_age','q_area']

class Page4(Page):
    form_models='player'
    
class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page1,Page2,Page3,Page4]
