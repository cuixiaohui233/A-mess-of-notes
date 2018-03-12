### 填昨天的坑
### 换了新的工作，本来应该有有面试总结，可是面试就问了三个问题：</br>
1.手写一个函数来实现求一个数的n次方；</br>
2.深拷贝，哈哈哈；</br>
3.给一个数组，里面全是整数，然后写一个函数，让技术排左边，偶数排右边；</br>
还有一个开放性的问题，所用技术栈里用的最好的是什么？react。react里面最熟悉的是什么？redux(当然是这个！！)，然后就一通说....从创建store到connect连接组件与store,说了最重要的点，保证整个应用只有一个store，而且数据是不可变的，这一次的数据，上一次的数据，下一次的数据，就不是同一份，顺便提了Immutable（哈哈哈）,
然后来聊到项目的时候，说到了又历史回退的功能，顺便说了数据不可变的重要性，面试官表示很赞同，哈哈哈，然后问我有什么问题，我说用啥技术栈，团队有多少成员......被问到这种问题真的不知道该咋说......
整个面试很潦草的感觉，哈哈哈，顺利通过，以后写电商的项目，第一次接触，努力努力再努力吧！</br>
### 接下来着重了解的知识：</br>
1.webpack</br>
2.less</br>
2.正则的基础知识得复习一下了</br>
3.移动端的适配问题,新工作会用到吧</br>
膜拜老铁和大神的总结...不过我也在努力啦...</br>
回到正题，填坑！！！</br>
是react-inl的坑...</br>
总结一下,如果是`<div>今天很兴奋...</div>`这种形式的话，那么直接使用api就好了，这里有个[链接](http://blog.csdn.net/function__/article/details/72778964)
但是如果是变量的话，那么...只有自己写一个reducer,然后调用config的里面配置了...
### 关于webpack,开始学习...
## 1.基本概念and核心概念</br>
·入口文件（entry）：</br>
就是打包开始的入口起点(我的理解)，最简单的例子:</br>

    moudle.exports = {</br>
        entry:'/path/app.js'
    }

单个入口的写法：</br>

    const config = {
        entry:'/path/app.js'
    }
    module.exports = config;

或者：<br/>

    const config = {
      entry: {
        main: './path/to/my/entry/file.js'
      }
    }
对象写法：</br>

    const config = {
        entry : {
            app:'/path/app.js',
            other:'/path/siderbar.js'
        }
    }

分离应用程序(app)和第三方库（vendar）(适合单页面应用)：</br>

    const config = {
        app:'/path/app.js',
        vendar:'/path/verdar.js'// 第三方库
    }
多页面应用程序：</br>

    const config = {
        entry:{
            pageOne:'/path/one.js',
            pageTwo:'/path/two.js',
            pageThree:'/path/three.js'
        }
    }


·出口文件（output）:<br/>
就是在哪里输出创建好的 bundles文件<br />

    const path = require('path');
    module.export = {
        entry:'/path/app.js',
        output:'
            path:path.resolve(_diename,'dist'),
            filename:'my-first-webpack-bundle.js'
        '
    }
上面的例子告诉我们，生成的打包文件放在那里，路径，还有打包生成的的文件的名字是什么.<br/>
如果有多个入口起点？<be/>

    entry:{
        app:'/path/app.js',
        search:'/path/search.js'
    },
    output:{
        filename:'[name].js',
        path:_dirname + '/dist'
    }

以上是将两个入口文件 app.js,search.js 写入到硬盘：./dist/app.js,./diat/search.js<br/>


·loader,由于webpack只理解JavaScript代码，所以需要loader去处理那些代码，可已将所有文件转换为webpack能处理的有效模块<br/>
loader有两个目标：<br/>
1.test属性，用于标识出要抓换的文件的类型（后缀名，是个正则表达式）<br/>
2.use属性，标识进行转换时用哪个loader;<br/>
在使用时需要下载哦：<br/>
`npm i --save-dev css-loader`<br/>

    const psth = rquire('path');
        entry:'/path/app.js',
        output:{
            path:path.resolve(_dirname,'dist'),
            filename:'bundle.js'
        },
        module:{
            rules:[
                { test:/\.test$/, use:'raw-loader'}
            ]
        }
    }

webpack允许你指定多个loader，而且代码简洁，可以让你看到整个loader的结构.<br/>

    module:{
        rules:[
            test:/\.css$/,
            use:[
                { loader:'style-loader'},
                {
                    loader:'css-loader',
                    options:{
                        moudle:true
                    }
                }
            ]
        ]
    }

接下来是插件：<br/>
·plugns,loader被用于转换某些类型的模块，而插件则可以用于执行范围更广的任务，用途很广，比如热加载的插件。要想使用一个插件，只需要`require()`，然后把它添加到`plugins`中就可以了，但是在添加之前需要`new`<br/>

        const Html = require('html-webpack-plugin');// 通过 npm 安装
        const webpack = require('webpack');// 访问内置的插件
        consr path = require('path');

        const config = {
            entry:'/path/app.js',
            output:{
                path:path.resove(_dirname,'dist'),
                filename:'bundle.js'
            },
            module:{
                loader:[
                    {
                        test:/\.css$/,
                        use:'css-loader'
                    }
                ]
            },
            plugins:[
                new webpack.optimize.UglifyPligin(),
                new HtmlWebpackPlugin({template:'./src/index.html'})
            ]
        }

        module.exports = config;

### es6 的 async 函数：
明天总结...