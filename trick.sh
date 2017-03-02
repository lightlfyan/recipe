
# 判断过滤字符串
string="fo1obar"

if grep -vq "/usr/local/bin" <<< $PATH; then
        export PATH=$PATH:/usr/local/bin
fi
