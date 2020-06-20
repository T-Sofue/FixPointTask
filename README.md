# FixPoint Task
このプログラムはフィックスポイント プログラミング試験問題の解答です。
<p>Tested Environment: Python 3.7.4</p>
<p>Program should run in Python version 3.x</p>
<h3>In this program the following features are introduced:</h3>
<ul>
  <li>User can mine logfile without the limitation of memory size</li>
  <li>Multiple logfiles can be opened for mining</li>
  <li>Logfile data can be searched by date</li>
  <li>List the remotehost in the order of most accessed</li>
  <li>List the Timestamp of accessed time</li>
</ul>
<h3>How to Use</h3>
<ol>
  <li>Install Python 3.x (preferably version3.7.4)</li>
  <li>Download and unzip "FixPointTask-master"</li>
  <li>In command line move to directory with "task4.py"</li>
  <li>run "python task4.py --directory name" to execute program</li>
  <li>Enter Y/N (y/n) to mine logfile based on date</li>
  <p></p>
  <p>run "python task4.py singlefile" which contains single logfile</p>
  <p>run "python task4.py multifile" which contains two logfiles</p>
</ol>
<h3>Result</h3>
<p>following text should appear on screen</p>
<ul>
  <p>remotehost: access count</p>
  <p>10.2.3.4: 3</p>
  <p>timstamp, access count</p>
  <p>18/4/2005:00:10:47: 3</p>
  <p>Mine Data By Date? Y/N</p>
  <p>Y</p>
  <p>Enter Query Date ; Y/M/D-Y/M/D</p>
  <p>eg. 2005/4/1-2005/4/30</p>
  <p>Input: 2005/4/1-2005/4/30</p>
  <p>query result(s)</p>
10.2.3.4 - - [18/Apr/2005:00:10:47 +0900] "GET / HTTP/1.1" 200 854 "-" "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)"

10.2.3.4 - - [18/Apr/2005:00:10:47 +0900] "GET /style.css HTTP/1.1" 200 102 "http://www.geekpage.jp/" "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)"

10.2.3.4 - - [18/Apr/2005:00:10:47 +0900] "GET /img/title.png HTTP/1.1" 304 - "http://www.geekpage.jp/" "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)"
</ul>
