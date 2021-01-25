import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SunburstEffectsComponent } from './sunburst-effects.component';

describe('SunburstEffectsComponent', () => {
  let component: SunburstEffectsComponent;
  let fixture: ComponentFixture<SunburstEffectsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SunburstEffectsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SunburstEffectsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
