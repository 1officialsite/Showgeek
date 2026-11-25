import re
# 1) Tema: ocupa tambem a area do notch/camera
p = 'android/app/src/main/res/values/styles.xml'
s = open(p, encoding='utf-8').read()
s = s.replace('</style>', '    <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>\n    </style>')
open(p, 'w', encoding='utf-8').write(s)

# 2) MainActivity: modo imersivo (esconde barras de status e navegacao)
p = 'android/app/src/main/java/com/showgeek/arena/MainActivity.java'
s = open(p, encoding='utf-8').read()
code = '''public class MainActivity extends BridgeActivity {
    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            getWindow().getDecorView().setSystemUiVisibility(
                android.view.View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | android.view.View.SYSTEM_UI_FLAG_FULLSCREEN
                | android.view.View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | android.view.View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | android.view.View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | android.view.View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION);
        }
    }
}'''
s2 = re.sub(r'public class MainActivity extends BridgeActivity\s*\{\s*\}', code, s)
assert s2 != s, 'MainActivity nao encontrada'
open(p, 'w', encoding='utf-8').write(s2)
print('ok')
