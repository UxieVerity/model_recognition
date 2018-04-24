var Canvas2Image = function () {

    function scaleCanvas (canvas, width, height) {
        var w = width,
            h = height;
        var retCanvas = document.createElement('canvas');
        var retCtx = retCanvas.getContext('2d');
        var $img = document.getElementById('img');
        var rate = $img.width/$img.naturalWidth;
        var cut_height = $('#img_div').scrollTop()/rate;
        retCanvas.width = width;
        retCanvas.height = height - cut_height;
        retCtx.drawImage(canvas, 0, cut_height, w, h, 0, 0, width, height);
        /*
        drawImage中的变量意义以此为
        {
            获取的图片dom
            图片向左的偏移量
            图片向上的偏移量，此处利用此属性，向上偏移了滚动条的位移距离，模拟裁剪效果
            图片横向拉伸，数值越小，拉伸程度越高，为原本图片的宽时，不拉伸
            图片纵向拉伸，数值越小，拉伸程度越高，为原本图片的长时，不拉伸
            图片向右的偏移量
            图片向下的偏移量
            图片的宽
            图片的长
        }
        */
        return retCanvas;
    }

    function getDataURL (canvas, type, width, height) {
        canvas = scaleCanvas(canvas, width, height);//将截取的图片填充到canvas
        return canvas.toDataURL(type);//将canvas转化为“type”型的图片
    }

    function genImage(strData) {
        var img = document.createElement('img');//创建新的img标签存放截取的图片
        img.width = $('#img_div').width();//设置图片的宽度
        img.id = "cut";//设置id
        img.src = strData;//设置src
        return img;
    }

    function fixType (type) {
        type = type.toLowerCase().replace(/jpg/i, 'jpeg');
        var r = type.match(/png|jpeg|bmp|gif/)[0];
        return 'image/' + r;
    }

    var convertToImage = function (canvas, width, height, type) {
        type = fixType(type);//截取的图片的类型设定
        var strData = getDataURL(canvas, type, width, height);
        return genImage(strData);
    };

    return {
        convertToImage: convertToImage
    };

}();