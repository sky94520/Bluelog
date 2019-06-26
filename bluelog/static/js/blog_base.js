//数据
let Main = {
    el: "#nav",
    data:{
        activeIndex: activeIndex
    }
    ,
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
            //跳转链接
            let id = "blog";
            if (key == 1)
                id = "blog";
            else if (key == 3)
                id = 'about';

            window.location.href = document.getElementById(id).getAttribute('href');
        }
    }
};

let nav = new Vue(Main);
