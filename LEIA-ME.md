# SHOW GEEK – Nova Arena (APK)

O jogo está em `www/index.html`. Dois jeitos de gerar o APK:

## A) Sem instalar nada (GitHub)
1. Crie um repositório no GitHub e envie todo o conteúdo desta pasta (incluindo `.github`).
2. Abra a aba **Actions**, rode **Build APK** (ou espere o push disparar).
3. Ao terminar, baixe `show-geek-apk` em *Artifacts* e instale o `app-debug.apk` no celular.

## B) No seu PC (Node 18+, JDK 17 e Android Studio/SDK)
```
npm install
npx cap add android
npx cap sync android
cd android && ./gradlew assembleDebug
```
APK em `android/app/build/outputs/apk/debug/app-debug.apk`.

Se rodar no PC, execute também `python3 tools/fullscreen.py` depois do `npx cap sync android` (tela cheia).

Para atualizar o jogo: troque `www/index.html` e rode `npx cap sync android` de novo.
Para publicar na Play Store é preciso um build *release* assinado.
