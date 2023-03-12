# Bootstrap

* 프론트엔드에서 유명한 사이트, 반응형 그리드 시스템 prebuild component(이미 만들어진 것)들이 많아 사용이 편리하다.

* Bootstrap 공식문서에서 원하는 것을 찾아 복붙하면 기본적인 것은 끝

* 같은 태그를 사용하더라도 html과 bootstrap은 시각적으로 다르게 보일 수 있다.

* 헤드에 링크 넣기
  
  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  ```

* 바디 마지막 줄에 스크립트 넣기 
  
  ```html
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
  ```

* Bootstrap 사용방법
  
  1. CDN을 사용하여 링크로 사용하는 방법
  
  2. Bootstrap에서 제공하는 css파일을 직접 다운받아 사용하는 방법

## CND

Content Delivery(Distribution) Network

* 컨텐츠(CSS, JS, image, Text 등)을 효율적으로 전달하기 위해 여러노드를 가진 네트워크에서 데이터를 제공하는 시스템

* CDN은 기본적으로 분산되어 있음, 따라서 사용자와 가까운 곳에서 컨텐츠를 전달받음

* 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)

* 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

* 장점: 내 컴퓨터에 파일이 없어도 링크로 받아오기가 가능하다

## spacing

* .mt-1  : 부트스트랩이 사용하는 클래스명
  
  * .(class)m(margin)t(top)-1(숫자같은 역할)
  
  * 1 = 0.25rem

* 단위
  
  * 일반적으로 px, % 를 사용
  
  * veiwport: 브라우저 창의 보이는 부분
    
    * vw: veiwport + width: 
    
    * vh: veiwport + height:
    
    * 100vw: veiwport의 넓이의 100퍼를 갖는 넓이
    
    * 50vw: veiwport의 넓이의 50퍼를 갖는 넓이
  
  * rem: 상대적 단위
    
    * html 태그가 가지고 있는 폰트사이즈(기본 16px)에 비례하여 작동 (폰트가 아닌것도 적용가능)
    
    * 10rem=160px
    
    * 0.5rem=8px

* .mx-0 : x(좌우)

* .my-0  y(상하)

* .mx-auto: 가운데 정렬

* .ms-auto : 오른쪽 정렬 (ms(start))

* .py-0: padding (좌우)=0

마진 상쇄현상 겹침 현상: 마진이 겹칠경우 가장 큰 마진만 반영

x: margin left right(좌우)

* 폰트 바꾸는 방법
  
  - font-family 사용
    
    첫번째가 안되면 그 다음 그다음 이렇게 사용하기 위해 font-family 사용
    
        h1{
                font-family: 'Courier New', Courier, monospace;
            }
  * 만약, 무조건 원하는 폰트를 사용하고 싶다면?? @font-face 사용
    
        @font-face {
                font-family: '원하는 폰트' ;
                src: url('CDN 넣');
            }
        
            h1{
                font-family: '원하는 폰트';
            }

## color

* bootstrap에서 customize-color검색

* mb-5와 mt-3의 영역이 겹쳤을 때 마진 상쇄현상(겹침 현상) 발생: 
  
  마진 상쇄현상(겹침 현상): 마진이 겹칠 경우 가장 큰 마진만 반영
  
  <박스 정렬>

```html
<body>

    <div class="box mb-4"></div>
    <div class="box mt-4 mx-auto bg-primary"></div>
    <div class="box mt-4 bg-success"></div>
    <div class="box mt-4 ms-auto bg-danger"></div>
    <div class="box mt-4 mb-5 bg-warning"></div>
    <div class="box mt-3"></div>  
</body>
```

```css
.box{
    width: 100px;
    height: 100px;
    background-color: orange;
}
```

<글자 정렬>

text-start(왼쪽), text-center(중앙), text-end(오른쪽) fs=폰트 크기

```html
<body>

    <P class="text-start fs-1">Apple</P>
    <p class="text-center fs-3">Banana</p>
    <p class="text-end fs-5">Orange</p>

</body>
```

<Carousel> - 이미지 여러개를 넘기면서 보기

```html
<body>
    <div id="carouselExample" class="carousel slide">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="img/img_1.png" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="img/img_2.jpeg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="img/img_3.jpeg" class="d-block w-100" alt="...">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
```

<

```html
<body>
    # d-flex: display-flex, justify-content-around: 메인축, content간격around
    # fs: font-size, text-white: 글씨 색
    <div class="d-flex justify-content-around fs-3 mt-3 ">

        <div class="bg-primary text-white">Home</div>
        <div>Produce</div>
        <div>Price</div>
        <div>Contact</div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
```

## 부트스트랩을 쓰는 가장 큰 이유 중 하나

### 반응형 웹페이지를 만드는데 편리하다

* 다양한 화면 큳기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장

* 반응형 웹은 별도의 기술 이름이 아닌 웹디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어

* 예시: media Queries. Flexbox, Bootstrap, Grid System, The viewpoint meta tag

### Grid System

* CSS가 아닌 편집 디자인에서 나온 개념으로 구성요소를 잘 배치하여 시각적으로 좋은 결과물을 만들기 위함

* 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인한다.

* 정보의 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

* 기본요소
  
  * Column: 실제 컨텐츠를 포함하는 부분
  
  * Gutter: 칼럼과 칼럼 사이의 공간(사이 간격)
  
  * Container: Column들을 담고 있는 공간

### Bootstrap Grid System

* Bootstrap Grid System은 flexbox로 제작된다.

* container, rows, column으로 컨텐츠를 배치하고 정렬한다.

* column은 12칸으로 고정되어있다.

* grid breakpoints는 6개이다.

* offset은 column12칸 중에 공백을 넣을 때 사용한다.

```html
<body>
    <div class="container">
        <div class="row">
        # class="col-sm-2 bg-primary"에서 sm사이즈 이상에서는 5를 해주세요라는 의
            <div class="col-sm-6 col-lg-5 bg-primary">1</div>
            <div class="col-sm-6 col-lg-2 bg-warning">2</div>
            <div class="         col-lg-5 bg-success">3</div>

        </div>

    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
</body>
```

class="col-sm-2 bg-primary"에서 sm사이즈 이상에서는 5를 해주세요(사이즈를 위한 )

sm사이즈보다 창이 작으면 col-sm-2가 적용되지 않음
