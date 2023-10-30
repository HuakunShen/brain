---
title: Tauri Local Server
---

Sometimes you may want to run a local server with the desktop app.

Actix is a good choice.

Here is sample code. You can run the server in a separate thread in setup.

```rust
use actix_web::dev::Server;
use std::error::Error;
use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};

#[get("/")]
pub async fn index() -> impl Responder {
    HttpResponse::Ok().body("App Name")
}

#[post("/echo")]
pub async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

pub fn run_server(port: u16) -> Result<Server, Box<dyn Error>> {
    Ok(HttpServer::new(|| App::new().service(index).service(echo))
        .bind(("0.0.0.0", port))?
        .run())
}

pub fn start_server() -> Result<(), Box<dyn Error>> {
    tauri::async_runtime::spawn(run_server(8000)?);
    Ok(())
}


pub fn setup(app: &mut tauri::App) {
    server::start_server().expect("Failed to start local server");
}

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            setup::setup(app);
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```
