# CSS Layout

 웹사이트 개발에 필요한 일반적인 구조가 있음



## Float

* 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping하도록 함

* 요소가 Normal flow를 벗어나도록함 

### Float  속성

* none: 기본값

* left: 요소를 왼쪽으로 띄움

* right: 요소를 오른쪽으로 띄움

### Float 예시

```html
<body>
    <div class="container">
        <div class="box"></div>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi, repellat quos magni aspernatur consequuntur pariatur esse, sed velit maiores, repudiandae accusantium id distinctio laborum alias! Dolore, ad non. Ipsa obcaecati iure adipisci. Deserunt consectetur repellendus doloribus modi? Rerum doloremque doloribus adipisci ullam aperiam animi aliquid. Nam, dignissimos atque, enim cum maxime consequatur soluta reiciendis impedit aliquid, ex ratione animi corporis saepe ducimus quod dolor placeat sint quibusdam assumenda quaerat. Quas nisi odit quod aspernatur sint consectetur nam ut iusto alias mollitia similique obcaecati rerum, itaque, ducimus beatae saepe architecto modi magni cum? Eaque iusto provident ipsum magni, cum nihil necessitatibus fugiat temporibus inventore veniam beatae asperiores, adipisci autem, veritatis delectus dolore consequuntur at a? Ex natus ipsam iste. Corrupti atque earum aliquam quos quod sequi sit mollitia illo libero fugiat provident eveniet optio unde, iste voluptates a impedit omnis eaque ducimus saepe? Hic, labore laudantium, exercitationem architecto, totam quas sunt nulla tempore doloribus sed fugit minima voluptatum eligendi. Dicta numquam tempore debitis ipsum aliquam a sit, pariatur quos sunt veniam itaque eos nobis ullam! Pariatur maiores laborum voluptate dolor nostrum, unde sequi sunt dolores, tempora ut quasi vero optio doloremque eum cupiditate vel ab iusto at asperiores illo nisi repellat, possimus tenetur! Suscipit molestias temporibus eius iste voluptas nam impedit odio! Mollitia ducimus culpa maiores, minima modi cum explicabo non totam saepe numquam omnis assumenda autem nesciunt voluptas? Sequi, magnam! Veritatis iusto similique tempore consequatur, ipsum tempora possimus, est, quibusdam consequuntur ipsam aut? Harum ab magni tempore, rem dolores nihil eos recusandae eligendi magnam voluptatum, porro pariatur blanditiis quisquam ipsam consequatur. Molestias, nesciunt. Cum impedit ipsam tenetur hic, reprehenderit commodi maxime vitae architecto fuga quos natus, aperiam id magnam veniam ab? Et quisquam quidem velit accusantium reiciendis molestias! Laudantium vel aliquam eius sequi beatae porro cupiditate fugiat molestiae tempore obcaecati.</p>


    </div>
```

```css
.box{
    width: 100px;
    height: 100px;
    background-color: orange;
    float: left; # 박스를 왼쪽으로
    margin-right: 10px;    #박스의 오른쪽에 margin으로 여백을 줌
}
```

```html
<body>
    <div class="container">
        <div class="box1 left"></div>
        <div class="box1 box2 left"></div>
        #box1, box2로 시작
    </div>
    
</body>
```

```css
.box1{ #box1잉 들어간 모든 요소에 적용
    width: 100px;
    height: 100px;
    background-color: orange;
    border: 1px solid black;
}
.box2{
    background-color: #ffff00;
    width: 200px;
}
.left{ # 박스를 왼쪽으로
    float: left;
} # 둘다 float한 상태라면 옆으로 나란히 붙음, 하나만 float한 상태라면 밑으로 겹쳐짐
```

##### float를 활용한 레이아웃 만들기

```html
<body>
    <div class="container">
        <div class="header"></div>
        <div class="section-left"></div>
        <div class="section-right"></div>
        <div class="footer"></div>

    </div>
</body>
```

```css
.header{
    height: 100px;
    background-color: yellow;
}
.section-left{
    height: 500px;
    background-color: bisque;
    width: 30%; # 전체에서 차지하는 비율
    float: left; # 왼쪽

}
.section-right{
    height: 500px;
    background-color: salmon;
    width: 70%;
    float: right;

}
.footer{
    clear: both;   # 없다면 header의 밑에 footer가 붙어서 section에 가려 보이지 않는다.
    height: 100px;
    background-color:darkorange;
}
```

### Float 정리

* 예전에는 Float는 레이아웃을 구성하기 위해 필수적으로 활용되었으나, 최근 Flexbox, Grid 등장과  함께 사용도가 낮아짐

* Float활용 전략-  Normal Flow에서 벗어난 레이아웃 구성
  
  + 원하는 요소들을 Float로 지정하여 배치

## Flexbox

Layout을 위해 탄생

원래 수동값의 부여 없이는 수직정렬, 아이템의 간격 배치가 어려웠다.

각각의 아이템이 저마다의 높이를 가지고 있을 때 레이아웃(높이)을 맞추기 힘들었다.

### CSS Flexible Box Layout

* 행과 열의 형태로 아이템들을 배치하는 1차원 레이아웃 모델

* 컨테이너를 두고 안의 아이템을 컨테이너를 사용하여 배치, 정렬

* 축
  
  * main axis(메인 축) : 아이템들이 쌓이는 방향(사용자의 결정)
  
  * cross axis(교차 축) : 메인축에 직각이 되는 축

* 구성요소
  
  * Flex Container(부모 요소)
    
    * flex 레이아웃을 형성하는 가장 기본적인 모델
    
    * flex item들이 좋여 있는 영역
    
    * display 속성을 flex 혹은 inline-flex로 지정
  
  * Flex item(자식 요소)
    
    * 컨테이너에 속해있는 컨텐츠(박스)

#### flexbox 활용

```html
<div class="container"> # 기본적으로 세로로 배열됨
        <div class="item">1</div>
        <div class="item">2</div>
        <div class="item">3</div>
        <div class="item">4</div>
        <div class="item">5</div>

    </div>
```

```css
.container{
    display: flex; 
    /* flex-direction: column-reverse; */
    flex-wrap: wrap;
    justify-content: space-evenly;
}

.item{
    width: 100px;
    height: 100px;
    background-color: pink;
    margin-top: 20px;
    margin-right: 20px;
    font-size: 50px;
}
```

##### 방향 설정

* display: flex
  
  flex 아이템들은 가로로 배치되고  자신이 가진 내용물의 width만큼만 차지한다.
  
  height는 컨테이너의 높이만큼 늘어난다.

* flex-direction:row (flex 설정시 기본값)
  
  메인축은 왼쪽에서 오른쪽으로 교차축은 위에서 아래로 진행 

* flex-direction: row-reverse
  
  아이템이 역순으로 가로배치, 역방향의 경우 보이는 것과 코드의 순서가 다르다.

* flex-direction: column
  
  아이템이 세로 방향 배치

* flex-direction: column-reverse
  
  아이템이 역순으로 세로 배치

* flex-wrap: nowrap(기본값)
  
  줄바꿈을 하지 않음 , 컨테이너가 작아질경우, 아이템들이 작아지다가 넘치면 벗어난다.

* flex-wrap: wrap
  
  컨테이너가 작아지더라도 아이템은 작아지지 않고 줄넘김 처리한다.

* flex-wrap: wrap-reverse
  
  컨테이너가 아이템 크기보다 크다면 그대로이나 작아져서 줄바꿈이 필요해지면 역순으로 정렬된다.

* flex-flow: row wrap; 
  
  flex-direction과 flex-wrap을 한꺼번에 지정할 수 있다.

* 메인축 방향 정렬(justify-content)
  
  * justify-content: flex-start 
    
    아이템들을 시작점으로 정렬
    
    row(가로 배치)일때는 왼쪽, column(세로 배치)일때는 위쪽
  
  * justify-content: flex-end
    
    아이템들을 끝점으로 정렬
    
    row(가로 배치)일때는 오른쪽, column(세로 배치)일때는 아래쪽
  
  * justify-content: center
    
    아이템을 가운데 정렬
  
  * justify-content: space-between
    
    아이템들 사이에 균일한 간격을 만든다.
    
    |-A----B----C----D-| 양끝을 제외아고 아이템간의 간격 중요
  
  * justify-content: space-around
    
    아이템들의 둘레에 균일한 간격을 만든다.
    
    |--A----B----C----D--| 모든요소의 좌우에 같은 간격이 설정되었음 끝부분 간격보다 요소간 간격이 2배이다.
  
  * justify-content: space-evenly
    
    아이템들의 사이와 양끝에 균일한 간격을 만든다.
    
    |----A----B----C----D----| 양끝부터 요소간 모든 간격이 동일하다.
    
    IE와 엣지(Edge)는 미지원
    
    

* 수직(교차)축 방향 정렬(align-items)

    <body>
        <div class="container">
            <div class="item">apple</div>
            <div class="item">banananananananannana</div>
            <div class="item">meloooooooooooon</div>
            
        </div>
    </body>

    .container{
        display: flex;
        background-color: bisque;
        height: 300px;
    }
    
    .item{
        background-color: orange;
        border: 1px solid black;
        font-size: 20px;
        margin-right: 5px;
    }
    

* align-items: stretch(기본값)
  
  아이템들이 수직축 방향으로 끝까지 늘어남(컨테이너의 높이만큼)

* align-items: flex-start
  
  아이템들을 시작점으로 정렬, content만큼만 차지함
  
  row(가로 배치)일때는 위쪽, column(세로 배치)일때는 왼쪽

* align-items: flex-end
  
  아이템들을 끝점으로 정렬
  
  row(가로 배치)일때는 아래쪽, column(세로 배치)일때는 오른쪽

* align-items: center
  
  아이템들을 가운데로 정렬

* align-items: baseline
  
  아이템들을 텍스트 베이스라인 기준으로 정렬, flex-start와는 다름

justify-content: center;  align-items: center; 를 같이 사용하면 아이템이 한가운데 놓임
