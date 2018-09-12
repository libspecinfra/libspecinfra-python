docker run --rm --user "$(id -u)":"$(id -g)" -v "$PWD/specinfra":/usr/src/specinfra -w /usr/src/specinfra rust cargo build --release
cp specinfra/target/release/libspecinfra.so ./libspecinfra/
