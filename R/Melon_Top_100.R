# 멜론 인기순위 TOP 100 곡들의 가사를 크롤링한다.

# 1.  멜론 차트 순위에서 순위/곡명/가수이름을 가져온다.
library(rvest)
url <- "https://www.melon.com/chart/index.htm"
text <- read_html(url,  encoding="utf-8")
# 어떤 이유에선지 불러와지지가 않는다.
library(httr)
http.standard <- GET('https://www.melon.com/chart/index.htm')
rank = html_nodes(read_html(http.standard), 'td:nth-child(2) > div > span.rank')
rank =  html_text(rank)
title = html_nodes(read_html(http.standard), 'td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
title =  html_text(title)

# 가수의 경우, 복수의 아티스트가 참가했을 때 해당 태그가 중복하여 여러 개가 검출되는 현상이 발생했다.
# singer = html_nodes(read_html(http.standard), '#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')

# 다소 복잡하지만 부모태그를 검출하여 이를 gsub로 다듬는 방식으로 해결한다.
singer = html_nodes(read_html(http.standard), 'td:nth-child(6) > div > div > div.ellipsis.rank02')
singer =  html_text(singer)
singer <- gsub("\t", "", singer)
singer <- gsub("\r\n", "", singer)

# 이렇게 하니 이름이 두 번 반복되어 저장되는 상황이 발생했다.
# 우선 각 벡터값에 대하여 이름 개수를 둘로 나눈 인덱스를 찾아낸다.
nchar(singer[1])/2
# 그다음 이를 이용해 슬라이싱 해준다.
substr(singer[1], 0, nchar(singer[1])/2)
# 이를 for문을 이용해 반복한다.
singer2 <- NULL
for (num in 1:100) {
  singer2 <- c(singer2, substr(singer[num], 0, nchar(singer[num])/2))
}

# 이제 순위/곡명/가수이름에 대한 자료가 모아졌다.
setwd("C:\Users\박찬희\Desktop\Git\TIL\R")
page <- cbind(rank, title, singer2)
write.csv(page, "top_100.csv")