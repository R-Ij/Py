<!DOCTYPE html>

{% block title %}Flask-Bootstrap{% endblock %}

{% block content %}
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="keywords" content="HTML5 Theme" />
        <meta name="description" content="Megakit - HTML5 Theme">
        <meta name="author" content="keenthemes.com">
        <!--<title>Boot</title>-->

        <!-- Web Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Lato:300,400,400i|Montserrat:400,700" rel="stylesheet">

        <!-- Vendor Styles -->
        <!--<link href="../static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>-->
        <link href="{{url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css')}}" rel="stylesheet" type="text/css"/>
          <link href="../static/css/animate.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/themify/themify.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/scrollbar/scrollbar.min.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/magnific-popup/magnific-popup.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/swiper/swiper.min.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/cubeportfolio/css/cubeportfolio.min.css" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='css/animate.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/themify/themify.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/scrollbar/scrollbar.min.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/magnific-popup/magnific-popup.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/swiper/swiper.min.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/cubeportfolio/css/cubeportfolio.min.css')}}" rel="stylesheet" type="text/css"/>

        <!-- Theme Styles -->
          <link href="../static/css/style.css" rel="stylesheet" type="text/css"/>
          <link href="../static/css/global/global.css" rel="stylesheet" type="text/css"/>
          <link href="../static/css/bootstrap.css" rel="stylesheet" type="text/css">
        <link href="{{url_for('static', filename='css/style.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='css/global/global.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='css/bootstrap.css')}}" rel="stylesheet" type="text/css"/>

        <!-- Favicon -->
        <!--<link rel="shortcut icon" href="../static/img/favicon.ico" type="image/x-icon">
        <link rel="apple-touch-icon" href="../static/img/apple-touch-icon.png">-->

        <!--========== JAVASCRIPTS (Load javascripts at bottom, this will reduce page load time) ==========-->
        <!-- Vendor -->
          <script type="text/javascript" src="../static/vendor/jquery.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.migrate.min.js"></script>
          <script type="text/javascript" src="../static/vendor/bootstrap/js/bootstrap.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.smooth-scroll.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.back-to-top.min.js"></script>
          <script type="text/javascript" src="../static/vendor/scrollbar/jquery.scrollbar.min.js"></script>
          <script type="text/javascript" src="../static/vendor/magnific-popup/jquery.magnific-popup.min.js"></script>
          <script type="text/javascript" src="../static/vendor/swiper/swiper.jquery.min.js"></script>
          <script type="text/javascript" src="../static/vendor/waypoint.min.js"></script>
          <script type="text/javascript" src="../static/vendor/counterup.min.js"></script>
          <script type="text/javascript" src="../static/vendor/cubeportfolio/js/jquery.cubeportfolio.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.parallax.min.js"></script>
          <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBsXUGTFS09pLVdsYEE9YrO2y4IAncAO2U"></script>
          <script type="text/javascript" src="../static/vendor/jquery.wow.min.js"></script>

        <!-- General Components and Settings -->
        <script type="text/javascript" src="../static/js/global.min.js"></script>
        <script type="text/javascript" src="../static/js/components/header-sticky.min.js"></script>
        <script type="text/javascript" src="../static/js/components/scrollbar.min.js"></script>
        <script type="text/javascript" src="../static/js/components/magnific-popup.min.js"></script>
        <script type="text/javascript" src="../static/js/components/swiper.min.js"></script>
        <script type="text/javascript" src="../static/js/components/counter.min.js"></script>
        <script type="text/javascript" src="../static/js/components/portfolio-3-col.min.js"></script>
        <script type="text/javascript" src="../static/js/components/parallax.min.js"></script>
        <script type="text/javascript" src="../static/js/components/google-map.min.js"></script>
        <script type="text/javascript" src="../static/js/components/wow.min.js"></script>

        <script type="text/javascript" src="../static/js/jquery.js"></script>
        <script type="text/javascript" src="../static/js/bootstrap.js"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/jquery.js')}}"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/bootstrap.js')}}"></script>
        <script type="text/javascript" src="/Users/lietachan913/node_modules/vue/dist/vue.min.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
        <script type="text/javascript" src="../static/js/vue.js"></script>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.1.1min.js"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/vue.js')}}"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/fl.js')}}"></script>
        <!--========== END JAVASCRIPTS ==========-->
    </head>

    <body>
        <!--========== HEADER ==========-->
        <header class="navbar-fixed-top s-header js__header-sticky js__header-overlay">
            <!-- Navbar -->
            <div class="s-header__navbar">
                <div class="s-header__container">
                    <div class="s-header__navbar-row">
<!--                        <div class="s-header__navbar-row-col">-->
<!--                            &lt;!&ndash; Logo &ndash;&gt;-->
<!--                            <div class="s-header__logo">-->
<!--                                <a href="index.html" class="s-header__logo-link">-->
<!--                                    <img class="s-header__logo-img s-header__logo-img-default" src="img/logo.png" alt="Megakit Logo">-->
<!--                                    <img class="s-header__logo-img s-header__logo-img-shrink" src="img/logo-dark.png" alt="Megakit Logo">-->
<!--                                </a>-->
<!--                            </div>-->
<!--                            &lt;!&ndash; End Logo &ndash;&gt;-->
<!--                        </div>-->
                        <div class="s-header__navbar-row-col">
                            <!-- Trigger -->
                            <a href="javascript:void(0);" class="s-header__trigger js__trigger">
                                <span class="s-header__trigger-icon"></span>
                                <svg x="0rem" y="0rem" width="3.125rem" height="3.125rem" viewbox="0 0 54 54">
                                    <circle fill="transparent" stroke="#fff" stroke-width="1" cx="27" cy="27" r="25" stroke-dasharray="157 157" stroke-dashoffset="157"></circle>
                                </svg>
                            </a>
                            <!-- End Trigger -->
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Navbar -->

            <!-- Overlay -->
            <div class="s-header-bg-overlay js__bg-overlay">
                <!-- Nav -->
                <nav class="s-header__nav js__scrollbar">
                    <div class="container-fluid">
                        <!-- Menu List -->
                        <ul class="list-unstyled s-header__nav-menu">
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider -is-active" href="index.html">Corporate</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">App Landing</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Portfolio</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Events</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Lawyer</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Clinic</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Coming Soon</a></li>
                        </ul>
                        <!-- End Menu List -->

                        <!-- Menu List -->
                        <ul class="list-unstyled s-header__nav-menu">
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">About</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Team</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Services</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Events</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">FAQ</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Contacts</a></li>
                        </ul>
                        <!-- End Menu List -->
                    </div>
                </nav>
                <!-- End Nav -->

                <!-- Action -->
                <ul class="list-inline s-header__action s-header__action--lb">
                    <li class="s-header__action-item"><a class="s-header__action-link -is-active" href="#">En</a></li>
                    <li class="s-header__action-item"><a class="s-header__action-link" href="#">Fr</a></li>
                </ul>
                <!-- End Action -->

                <!-- Action -->
                <ul class="list-inline s-header__action s-header__action--rb">
                    <li class="s-header__action-item">
                        <a class="s-header__action-link" href="#">
                            <i class="g-padding-r-5--xs ti-facebook"></i>
                            <span class="g-display-none--xs g-display-inline-block--sm">Facebook</span>
                        </a>
                    </li>
                    <li class="s-header__action-item">
                        <a class="s-header__action-link" href="#">
                            <i class="g-padding-r-5--xs ti-twitter"></i>
                            <span class="g-display-none--xs g-display-inline-block--sm">Twitter</span>
                        </a>
                    </li>
                    <li class="s-header__action-item">
                        <a class="s-header__action-link" href="#">
                            <i class="g-padding-r-5--xs ti-instagram"></i>
                            <span class="g-display-none--xs g-display-inline-block--sm">Instagram</span>
                        </a>
                    </li>
                </ul>
                <!-- End Action -->
            </div>
            <!-- End Overlay -->
        </header>

        <!--========== SWIPER SLIDER ==========-->
          <div class="s-swiper js__swiper-one-item">
              <!-- Swiper Wrapper -->
              <div class="swiper-wrapper">
                  <div class="g-fullheight--xs g-bg-position--center swiper-slide" style="background: url('../static/img/1920x1080/02.jpg');">
                      <div class="container g-text-center--xs g-ver-center--xs">
                          <div class="g-margin-b-30--xs">
                              <h1 class="g-font-size-35--xs g-font-size-45--sm g-font-size-55--md g-color--white">A Mobile Experience<br>That Inspires Travel</h1>
                          </div>
                          <a class="js__popup__youtube" href="https://www.youtube.com/watch?v=lcFYdgZKZxY" title="Intro Video">
                              <i class="s-icon s-icon--lg s-icon--white-bg g-radius--circle ti-control-play"></i>
                          </a>
                      </div>
                  </div>
                  <div class="g-fullheight--xs g-bg-position--center swiper-slide" style="background: url('../static/img/1920x1080/01.jpg');">
                      <div class="container g-text-center--xs g-ver-center--xs">
                          <div class="g-margin-b-30--xs">
                              <div class="g-margin-b-30--xs">
                                  <h2 class="g-font-size-35--xs g-font-size-45--sm g-font-size-55--md g-color--white">We Craft Experience<br>That Help Brands<br>Stand Out</h2>
                              </div>
                              <a class="js__popup__youtube" href="https://www.youtube.com/" title="Intro Video">
                                  <i class="s-icon s-icon--lg s-icon--white-bg g-radius--circle ti-control-play"></i>
                              </a>
                          </div>
                      </div>
                  </div>
              </div>
            <!-- End Swiper Wrapper -->

            <!-- Arrows -->
              <a href="javascript:void(0);" class="s-swiper__arrow-v1--right s-icon s-icon--md s-icon--white-brd g-radius--circle ti-angle-right js__swiper-btn--next"></a>
              <a href="javascript:void(0);" class="s-swiper__arrow-v1--left s-icon s-icon--md s-icon--white-brd g-radius--circle ti-angle-left js__swiper-btn--prev"></a>
            <!-- End Arrows -->

              <a href="#js__scroll-to-section" class="s-scroll-to-section-v1--bc g-margin-b-15--xs">
                  <span class="g-font-size-18--xs g-color--white ti-angle-double-down"></span>
                  <p class="text-uppercase g-color--white g-letter-spacing--3 g-margin-b-0--xs">Learn More</p>
              </a>
          </div>
        <!--========== END SWIPER SLIDER ==========-->

        <div class="page-header">
            {% if images %}
            <div class="container">
            <div class="row">
                <div class="col-md-6 col-md-offset-3">
                    <!-- カルーセル部分  -->
                    <div id="carousel1" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                              <li class="active" data-target="#carousel1" data-slide-to="0"></li>
                              <li data-target="#carousel1" data-slide-to="1"></li>
                              <li data-target="#carousel1" data-slide-to="2"></li>
                            {% for img in images %}
                                <li data-target="#carousel1" data-slide-to="{{ images.index(img) }}"></li>
                            {% endfor %}
                        </ol>
                        <div class="carousel-inner" role="listbox">
                            {% for img in images %}
                                {% if images.index(img) == 0 %}
                                    <div class="item active">
                                        <img src="../static/img/main/{{ img }}">
                                    </div>
                                {% else %}
                                    <div class="item">
                                        <img src="../static/img/main/{{ img }}">
                                    </div>
                                {% endif %}
                            {% endfor %}
                              <div class="item active">
                                  <img src="../static/img/main/1.jpg" alt="Desert">
                              </div>
                              <div class="item">
                                  <img src="../static/img/main/2.jpg" alt="Lighthouse">
                              </div>
                              <div class="item">
                                  <img src="../static/img/main/3.jpg" alt="Penguins">
                              </div>
                        </div>
                        <a class="left carousel-control" href="#carousel1" role="button" data-slide="prev">
                            <i class="material-icons"></i>
                            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                        </a>
                        <a class="right carousel-control" href="#carousel1" role="button" data-slide="next">
                            <i class="material-icons"></i>
                            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                        </a>
                    </div>
                </div>
            </div>
            </div>
            {% endif %}
        </div>

        <!-- ナビゲーションバー -->
        <nav class="navbar navbar-default"><!-- navbar-fixed-top -->
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-navi" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>

                <div class="collapse navbar-collapse" id="bs-navi">
                    <ul class="nav navbar-nav">
                        <li><a href="#">ホーム</a></li>
                        <li><a href="#">情報1</a></li>
                        <li><a href="#">情報2</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">会社情報<span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">sub1</a></li>
                                <li><a href="#">sub2</a></li>
                                <li><a href="#">sub3</a></li>
                                <li><a href="#">sub4</a></li>
                            </ul>
                        </li>
                        <li><a href="#">ブログ</a></li>
                        <li><a href="#">お問い合わせ</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- パンくずリスト -->
        <ol class="breadcrumb">
            <li><a href="/">HOME</a></li>
            <li><a href="/blog">ブログ</a></li>
            <li class="active">BootStrap</li>
        </ol>

        <!-- table -->
        <!-- Escape(Not Jinja Template) -->
        {% raw %}
        <a href="#" class="btn btn-info btn-sm">OK</a>
        <div id="msg">
            <table class="table table-hover table-striped">
                <tr><td>table</td><td>{{ vue_msg1 }}</td></tr>
                <tr><td>table-striped</td><td>{{ vue_msg2 }}</td></tr>
                <tr><td>table-bordered</td><td>テーブルとセルの全てのサイドに線をつける</td></tr>
                <tr><td>table-condensed</td><td>テーブルのセルの余白を狭くする</td></tr>
                <tr><td>table-hover</td><td>マウスがホバーした時に背景色が変わる</td></tr>
                <tr><td>(外側のdivタグで利用する)table-responsive</td><td>コンテンツ幅を超える部分はスクロールできるようにする</td></tr>
            </table>
        </div>
        {% endraw %}

        <!-- 入力フォーム -->
        <form method="post", action="/regist">
            <div class="form-group">
                <label for="name">氏名</label>
                <input type="email" class="form-control" id="name" placeholder="w-name">
            </div>
            <div class="form-group">
                <label for="message">メッセージ</label>
                <textarea name="message" rows="8" cols="80" class="form-control"></textarea>
            </div>
            <div class="form-group">
                <label for="date">日付</label>
                <select class="form-control" name="date">
                    <option value="select-date">2019年10月</option>
                    <option value="select-date">2019年11月</option>
                    <option value="select-date">2019年12月</option>
                </select>
            </div>
            <!--<button type="submit" class="btn btn-primary">登録する</button>-->
            <!-- モーダルウィンドウ -->
            <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#modal-1">登録する</button>
            <div class="modal fade" id="modal-1" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal"><span>×</span></button>
                            <h4 class="modal-title">title</h4>
                        </div>
                        <div class="modal-body">comment</div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">キャンセル</button>
                            <button type="button" class="btn btn-primary">決定</button>
                        </div>
                    </div>
                </div>
            </div>

        </form>

        <nav>
            <ul class="pagination">
                <li>
                    <a href="#" aria-label="前のページへ">
                    <span aria-hidden="true">«</span>
                    </a>
                </li>
                <li><a href="#">1</a></li>
                <li class="active"><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#">5</a></li>
                <li>
                    <a href="#" aria-label="次のページへ">
                        <span aria-hidden="true">»</span>
                    </a>
                </li>
            </ul>
        </nav>

        <!-- Vue.js -->
          <script>
          new Vue({
              el: '#msg',
              data:{
                  vue_msg1: 'Bootstrap用のスタイルのtableを使う(必須)',
                  vue_msg2: '1行ずつストライプのように背景色がつきます'
              }
          });
          </script>
        <!-- End Vue.js -->

    </body>
</html>
{% endblock %}<!DOCTYPE html>

{% block title %}Flask-Bootstrap{% endblock %}

{% block content %}
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="keywords" content="HTML5 Theme" />
        <meta name="description" content="Megakit - HTML5 Theme">
        <meta name="author" content="keenthemes.com">
        <!--<title>Boot</title>-->

        <!-- Web Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Lato:300,400,400i|Montserrat:400,700" rel="stylesheet">

        <!-- Vendor Styles -->
        <!--<link href="../static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>-->
        <link href="{{url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css')}}" rel="stylesheet" type="text/css"/>
          <link href="../static/css/animate.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/themify/themify.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/scrollbar/scrollbar.min.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/magnific-popup/magnific-popup.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/swiper/swiper.min.css" rel="stylesheet" type="text/css"/>
          <link href="../static/vendor/cubeportfolio/css/cubeportfolio.min.css" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='css/animate.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/themify/themify.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/scrollbar/scrollbar.min.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/magnific-popup/magnific-popup.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/swiper/swiper.min.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='vendor/cubeportfolio/css/cubeportfolio.min.css')}}" rel="stylesheet" type="text/css"/>

        <!-- Theme Styles -->
          <link href="../static/css/style.css" rel="stylesheet" type="text/css"/>
          <link href="../static/css/global/global.css" rel="stylesheet" type="text/css"/>
          <link href="../static/css/bootstrap.css" rel="stylesheet" type="text/css">
        <link href="{{url_for('static', filename='css/style.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='css/global/global.css')}}" rel="stylesheet" type="text/css"/>
        <link href="{{url_for('static', filename='css/bootstrap.css')}}" rel="stylesheet" type="text/css"/>

        <!-- Favicon -->
        <!--<link rel="shortcut icon" href="../static/img/favicon.ico" type="image/x-icon">
        <link rel="apple-touch-icon" href="../static/img/apple-touch-icon.png">-->

        <!--========== JAVASCRIPTS (Load javascripts at bottom, this will reduce page load time) ==========-->
        <!-- Vendor -->
          <script type="text/javascript" src="../static/vendor/jquery.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.migrate.min.js"></script>
          <script type="text/javascript" src="../static/vendor/bootstrap/js/bootstrap.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.smooth-scroll.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.back-to-top.min.js"></script>
          <script type="text/javascript" src="../static/vendor/scrollbar/jquery.scrollbar.min.js"></script>
          <script type="text/javascript" src="../static/vendor/magnific-popup/jquery.magnific-popup.min.js"></script>
          <script type="text/javascript" src="../static/vendor/swiper/swiper.jquery.min.js"></script>
          <script type="text/javascript" src="../static/vendor/waypoint.min.js"></script>
          <script type="text/javascript" src="../static/vendor/counterup.min.js"></script>
          <script type="text/javascript" src="../static/vendor/cubeportfolio/js/jquery.cubeportfolio.min.js"></script>
          <script type="text/javascript" src="../static/vendor/jquery.parallax.min.js"></script>
          <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBsXUGTFS09pLVdsYEE9YrO2y4IAncAO2U"></script>
          <script type="text/javascript" src="../static/vendor/jquery.wow.min.js"></script>

        <!-- General Components and Settings -->
        <script type="text/javascript" src="../static/js/global.min.js"></script>
        <script type="text/javascript" src="../static/js/components/header-sticky.min.js"></script>
        <script type="text/javascript" src="../static/js/components/scrollbar.min.js"></script>
        <script type="text/javascript" src="../static/js/components/magnific-popup.min.js"></script>
        <script type="text/javascript" src="../static/js/components/swiper.min.js"></script>
        <script type="text/javascript" src="../static/js/components/counter.min.js"></script>
        <script type="text/javascript" src="../static/js/components/portfolio-3-col.min.js"></script>
        <script type="text/javascript" src="../static/js/components/parallax.min.js"></script>
        <script type="text/javascript" src="../static/js/components/google-map.min.js"></script>
        <script type="text/javascript" src="../static/js/components/wow.min.js"></script>

        <script type="text/javascript" src="../static/js/jquery.js"></script>
        <script type="text/javascript" src="../static/js/bootstrap.js"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/jquery.js')}}"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/bootstrap.js')}}"></script>
        <script type="text/javascript" src="/Users/lietachan913/node_modules/vue/dist/vue.min.js"></script>
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>
        <script type="text/javascript" src="../static/js/vue.js"></script>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.1.1min.js"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/vue.js')}}"></script>
        <script type="text/javascript" src="{{url_for('static', filename='js/fl.js')}}"></script>
        <!--========== END JAVASCRIPTS ==========-->
    </head>

    <body>
        <!--========== HEADER ==========-->
        <header class="navbar-fixed-top s-header js__header-sticky js__header-overlay">
            <!-- Navbar -->
            <div class="s-header__navbar">
                <div class="s-header__container">
                    <div class="s-header__navbar-row">
<!--                        <div class="s-header__navbar-row-col">-->
<!--                            &lt;!&ndash; Logo &ndash;&gt;-->
<!--                            <div class="s-header__logo">-->
<!--                                <a href="index.html" class="s-header__logo-link">-->
<!--                                    <img class="s-header__logo-img s-header__logo-img-default" src="img/logo.png" alt="Megakit Logo">-->
<!--                                    <img class="s-header__logo-img s-header__logo-img-shrink" src="img/logo-dark.png" alt="Megakit Logo">-->
<!--                                </a>-->
<!--                            </div>-->
<!--                            &lt;!&ndash; End Logo &ndash;&gt;-->
<!--                        </div>-->
                        <div class="s-header__navbar-row-col">
                            <!-- Trigger -->
                            <a href="javascript:void(0);" class="s-header__trigger js__trigger">
                                <span class="s-header__trigger-icon"></span>
                                <svg x="0rem" y="0rem" width="3.125rem" height="3.125rem" viewbox="0 0 54 54">
                                    <circle fill="transparent" stroke="#fff" stroke-width="1" cx="27" cy="27" r="25" stroke-dasharray="157 157" stroke-dashoffset="157"></circle>
                                </svg>
                            </a>
                            <!-- End Trigger -->
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Navbar -->

            <!-- Overlay -->
            <div class="s-header-bg-overlay js__bg-overlay">
                <!-- Nav -->
                <nav class="s-header__nav js__scrollbar">
                    <div class="container-fluid">
                        <!-- Menu List -->
                        <ul class="list-unstyled s-header__nav-menu">
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider -is-active" href="index.html">Corporate</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">App Landing</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Portfolio</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Events</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Lawyer</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Clinic</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Coming Soon</a></li>
                        </ul>
                        <!-- End Menu List -->

                        <!-- Menu List -->
                        <ul class="list-unstyled s-header__nav-menu">
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">About</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Team</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Services</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Events</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">FAQ</a></li>
                            <li class="s-header__nav-menu-item"><a class="s-header__nav-menu-link s-header__nav-menu-link-divider" href="#">Contacts</a></li>
                        </ul>
                        <!-- End Menu List -->
                    </div>
                </nav>
                <!-- End Nav -->

                <!-- Action -->
                <ul class="list-inline s-header__action s-header__action--lb">
                    <li class="s-header__action-item"><a class="s-header__action-link -is-active" href="#">En</a></li>
                    <li class="s-header__action-item"><a class="s-header__action-link" href="#">Fr</a></li>
                </ul>
                <!-- End Action -->

                <!-- Action -->
                <ul class="list-inline s-header__action s-header__action--rb">
                    <li class="s-header__action-item">
                        <a class="s-header__action-link" href="#">
                            <i class="g-padding-r-5--xs ti-facebook"></i>
                            <span class="g-display-none--xs g-display-inline-block--sm">Facebook</span>
                        </a>
                    </li>
                    <li class="s-header__action-item">
                        <a class="s-header__action-link" href="#">
                            <i class="g-padding-r-5--xs ti-twitter"></i>
                            <span class="g-display-none--xs g-display-inline-block--sm">Twitter</span>
                        </a>
                    </li>
                    <li class="s-header__action-item">
                        <a class="s-header__action-link" href="#">
                            <i class="g-padding-r-5--xs ti-instagram"></i>
                            <span class="g-display-none--xs g-display-inline-block--sm">Instagram</span>
                        </a>
                    </li>
                </ul>
                <!-- End Action -->
            </div>
            <!-- End Overlay -->
        </header>

        <!--========== SWIPER SLIDER ==========-->
          <div class="s-swiper js__swiper-one-item">
              <!-- Swiper Wrapper -->
              <div class="swiper-wrapper">
                  <div class="g-fullheight--xs g-bg-position--center swiper-slide" style="background: url('../static/img/1920x1080/02.jpg');">
                      <div class="container g-text-center--xs g-ver-center--xs">
                          <div class="g-margin-b-30--xs">
                              <h1 class="g-font-size-35--xs g-font-size-45--sm g-font-size-55--md g-color--white">A Mobile Experience<br>That Inspires Travel</h1>
                          </div>
                          <a class="js__popup__youtube" href="https://www.youtube.com/watch?v=lcFYdgZKZxY" title="Intro Video">
                              <i class="s-icon s-icon--lg s-icon--white-bg g-radius--circle ti-control-play"></i>
                          </a>
                      </div>
                  </div>
                  <div class="g-fullheight--xs g-bg-position--center swiper-slide" style="background: url('../static/img/1920x1080/01.jpg');">
                      <div class="container g-text-center--xs g-ver-center--xs">
                          <div class="g-margin-b-30--xs">
                              <div class="g-margin-b-30--xs">
                                  <h2 class="g-font-size-35--xs g-font-size-45--sm g-font-size-55--md g-color--white">We Craft Experience<br>That Help Brands<br>Stand Out</h2>
                              </div>
                              <a class="js__popup__youtube" href="https://www.youtube.com/" title="Intro Video">
                                  <i class="s-icon s-icon--lg s-icon--white-bg g-radius--circle ti-control-play"></i>
                              </a>
                          </div>
                      </div>
                  </div>
              </div>
            <!-- End Swiper Wrapper -->

            <!-- Arrows -->
              <a href="javascript:void(0);" class="s-swiper__arrow-v1--right s-icon s-icon--md s-icon--white-brd g-radius--circle ti-angle-right js__swiper-btn--next"></a>
              <a href="javascript:void(0);" class="s-swiper__arrow-v1--left s-icon s-icon--md s-icon--white-brd g-radius--circle ti-angle-left js__swiper-btn--prev"></a>
            <!-- End Arrows -->

              <a href="#js__scroll-to-section" class="s-scroll-to-section-v1--bc g-margin-b-15--xs">
                  <span class="g-font-size-18--xs g-color--white ti-angle-double-down"></span>
                  <p class="text-uppercase g-color--white g-letter-spacing--3 g-margin-b-0--xs">Learn More</p>
              </a>
          </div>
        <!--========== END SWIPER SLIDER ==========-->

        <div class="page-header">
            {% if images %}
            <div class="container">
            <div class="row">
                <div class="col-md-6 col-md-offset-3">
                    <!-- カルーセル部分  -->
                    <div id="carousel1" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                              <li class="active" data-target="#carousel1" data-slide-to="0"></li>
                              <li data-target="#carousel1" data-slide-to="1"></li>
                              <li data-target="#carousel1" data-slide-to="2"></li>
                            {% for img in images %}
                                <li data-target="#carousel1" data-slide-to="{{ images.index(img) }}"></li>
                            {% endfor %}
                        </ol>
                        <div class="carousel-inner" role="listbox">
                            {% for img in images %}
                                {% if images.index(img) == 0 %}
                                    <div class="item active">
                                        <img src="../static/img/main/{{ img }}">
                                    </div>
                                {% else %}
                                    <div class="item">
                                        <img src="../static/img/main/{{ img }}">
                                    </div>
                                {% endif %}
                            {% endfor %}
                              <div class="item active">
                                  <img src="../static/img/main/1.jpg" alt="Desert">
                              </div>
                              <div class="item">
                                  <img src="../static/img/main/2.jpg" alt="Lighthouse">
                              </div>
                              <div class="item">
                                  <img src="../static/img/main/3.jpg" alt="Penguins">
                              </div>
                        </div>
                        <a class="left carousel-control" href="#carousel1" role="button" data-slide="prev">
                            <i class="material-icons"></i>
                            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                        </a>
                        <a class="right carousel-control" href="#carousel1" role="button" data-slide="next">
                            <i class="material-icons"></i>
                            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                        </a>
                    </div>
                </div>
            </div>
            </div>
            {% endif %}
        </div>

        <!-- ナビゲーションバー -->
        <nav class="navbar navbar-default"><!-- navbar-fixed-top -->
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-navi" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>

                <div class="collapse navbar-collapse" id="bs-navi">
                    <ul class="nav navbar-nav">
                        <li><a href="#">ホーム</a></li>
                        <li><a href="#">情報1</a></li>
                        <li><a href="#">情報2</a></li>
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">会社情報<span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#">sub1</a></li>
                                <li><a href="#">sub2</a></li>
                                <li><a href="#">sub3</a></li>
                                <li><a href="#">sub4</a></li>
                            </ul>
                        </li>
                        <li><a href="#">ブログ</a></li>
                        <li><a href="#">お問い合わせ</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- パンくずリスト -->
        <ol class="breadcrumb">
            <li><a href="/">HOME</a></li>
            <li><a href="/blog">ブログ</a></li>
            <li class="active">BootStrap</li>
        </ol>

        <!-- table -->
        <!-- Escape(Not Jinja Template) -->
        {% raw %}
        <a href="#" class="btn btn-info btn-sm">OK</a>
        <div id="msg">
            <table class="table table-hover table-striped">
                <tr><td>table</td><td>{{ vue_msg1 }}</td></tr>
                <tr><td>table-striped</td><td>{{ vue_msg2 }}</td></tr>
                <tr><td>table-bordered</td><td>テーブルとセルの全てのサイドに線をつける</td></tr>
                <tr><td>table-condensed</td><td>テーブルのセルの余白を狭くする</td></tr>
                <tr><td>table-hover</td><td>マウスがホバーした時に背景色が変わる</td></tr>
                <tr><td>(外側のdivタグで利用する)table-responsive</td><td>コンテンツ幅を超える部分はスクロールできるようにする</td></tr>
            </table>
        </div>
        {% endraw %}

        <!-- 入力フォーム -->
        <form method="post", action="/regist">
            <div class="form-group">
                <label for="name">氏名</label>
                <input type="email" class="form-control" id="name" placeholder="w-name">
            </div>
            <div class="form-group">
                <label for="message">メッセージ</label>
                <textarea name="message" rows="8" cols="80" class="form-control"></textarea>
            </div>
            <div class="form-group">
                <label for="date">日付</label>
                <select class="form-control" name="date">
                    <option value="select-date">2019年10月</option>
                    <option value="select-date">2019年11月</option>
                    <option value="select-date">2019年12月</option>
                </select>
            </div>
            <!--<button type="submit" class="btn btn-primary">登録する</button>-->
            <!-- モーダルウィンドウ -->
            <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#modal-1">登録する</button>
            <div class="modal fade" id="modal-1" tabindex="-1">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal"><span>×</span></button>
                            <h4 class="modal-title">title</h4>
                        </div>
                        <div class="modal-body">comment</div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">キャンセル</button>
                            <button type="button" class="btn btn-primary">決定</button>
                        </div>
                    </div>
                </div>
            </div>

        </form>

        <nav>
            <ul class="pagination">
                <li>
                    <a href="#" aria-label="前のページへ">
                    <span aria-hidden="true">«</span>
                    </a>
                </li>
                <li><a href="#">1</a></li>
                <li class="active"><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#">5</a></li>
                <li>
                    <a href="#" aria-label="次のページへ">
                        <span aria-hidden="true">»</span>
                    </a>
                </li>
            </ul>
        </nav>

        <!-- Vue.js -->
          <script>
          new Vue({
              el: '#msg',
              data:{
                  vue_msg1: 'Bootstrap用のスタイルのtableを使う(必須)',
                  vue_msg2: '1行ずつストライプのように背景色がつきます'
              }
          });
          </script>
        <!-- End Vue.js -->

    </body>
</html>
{% endblock %}