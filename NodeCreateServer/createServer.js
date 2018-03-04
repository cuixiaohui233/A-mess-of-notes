// ### 组成：
// 1.引入 require 模块：用此来载入模块
// 2.创建服务器：监听客户端的请求
// 3.接受请求与响应请求

// ### 创建 Node.js 应用：

// (1).引入 http 模块：用 require 来载入 http 模块
const http = require('http');
// (2).创建服务器：http.createServer() 方法创建服务器bi能够使用 listen 方法监听指定端口（自行指定）
// http.createServer() 方法有一个函数，函数通过 request 和 response 接收客户端发来的请求和响应数据
http.createServer(function(req,res){
  // req 是接收到的客户端的请求,res 是响应
  console.log(req);

  // 发送 HTTP 头部
  // HTTP 状态：200 -> ok
  // 内容类型：text/plain
  res.writeHead(200,{'Content-Type':'text/plain'})

  // 发送响应数据
  res.end('欢迎来到皇家别墅...')
}).listen(8888);
console.log('Server running at http://192.168.0.116:8888')
