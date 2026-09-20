import { ILLUSTRATIONS, SPRITE, type IllusKey } from "./illustrations";

export type { IllusKey };

export function IllustrationSprite() {
  return <svg width="0" height="0" style={{ position: "absolute" }} aria-hidden="true" focusable="false" dangerouslySetInnerHTML={{ __html: SPRITE }} />;
}

export function Illustration({ name, className }: { name: IllusKey; className?: string }) {
  const i = ILLUSTRATIONS[name];
  return <svg className={className} viewBox={`0 0 ${i.w} ${i.h}`} aria-hidden="true" focusable="false" dangerouslySetInnerHTML={{ __html: i.body }} />;
}
