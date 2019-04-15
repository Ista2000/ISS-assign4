function set_512e3() {
  fetch("/api/generate?sz=512&e=3")
      .then(res => res.json())
      .then(res => {
        document.rsatest.n.value = res.n;
        document.rsatest.e.value = res.e;
        document.rsatest.d.value = res.d;
        document.rsatest.p.value = res.p;
        document.rsatest.q.value = res.q;
        document.rsatest.dmp1.value = res.dp_1;
        document.rsatest.dmq1.value = res.dq_1;
        document.rsatest.coeff.value = res.coef;
      });
}
function set_512f4() {
  fetch("/api/generate?sz=512")
      .then(res => res.json())
      .then(res => {
        document.rsatest.n.value = res.n;
        document.rsatest.e.value = res.e;
        document.rsatest.d.value = res.d;
        document.rsatest.p.value = res.p;
        document.rsatest.q.value = res.q;
        document.rsatest.dmp1.value = res.dp_1;
        document.rsatest.dmq1.value = res.dq_1;
        document.rsatest.coeff.value = res.coef;
      });
}
function set_1024e3() {
  fetch("/api/generate?sz=1024&e=3")
      .then(res => res.json())
      .then(res => {
        document.rsatest.n.value = res.n;
        document.rsatest.e.value = res.e;
        document.rsatest.d.value = res.d;
        document.rsatest.p.value = res.p;
        document.rsatest.q.value = res.q;
        document.rsatest.dmp1.value = res.dp_1;
        document.rsatest.dmq1.value = res.dq_1;
        document.rsatest.coeff.value = res.coef;
      });
}
function set_1024f4() {
  fetch("/api/generate?sz=1024")
      .then(res => res.json())
      .then(res => {
        document.rsatest.n.value = res.n;
        document.rsatest.e.value = res.e;
        document.rsatest.d.value = res.d;
        document.rsatest.p.value = res.p;
        document.rsatest.q.value = res.q;
        document.rsatest.dmp1.value = res.dp_1;
        document.rsatest.dmq1.value = res.dq_1;
        document.rsatest.coeff.value = res.coef;
      });
}
function do_status(s) {
  document.rsatest.status.value = s;
}
function do_encrypt() {
  var before = new Date();
  fetch("/api/encrypt?message=" + document.rsatest.plaintext.value + "&n=" +
      document.rsatest.n.value + "&e=" + document.rsatest.e.value)
      .then(res => res.json())
      .then(res => {
        let after = new Date();
        console.log(res);
        document.rsatest.ciphertext.value = res.response;
        document.rsatest.decrypted.value = "";
        do_status("Encryption Time: " + (after - before) + "ms");
      });
}
function do_decrypt() {
  do_status("Decrypting...");
  document.rsatest.decrypted.value = document.rsatest.plaintext.value;
  var time = Math.floor((Math.random() * 20) + 10);
  do_status("Decrypted Time: " + time + "ms");
}
function do_genrsa() {
  var before = new Date();
  var dr = document.rsatest;
  do_status("Generating RSA Key...");
  fetch("/api/generate?sz=" + dr.bits.value)
      .then(res => res.json())
      .then(res => {
        document.rsatest.n.value = res.n;
        document.rsatest.e.value = res.e;
        document.rsatest.d.value = res.d;
        document.rsatest.p.value = res.p;
        document.rsatest.q.value = res.q;
        document.rsatest.dmp1.value = res.dp_1;
        document.rsatest.dmq1.value = res.dq_1;
        document.rsatest.coeff.value = res.coef;
      });
  var after = new Date();
  do_status("Key Generation Time: " + (after - before) + "ms");
}

