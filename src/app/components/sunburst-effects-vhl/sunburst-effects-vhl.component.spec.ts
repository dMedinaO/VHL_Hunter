import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SunburstEffectsVHLComponent } from './sunburst-effects-vhl.component';

describe('SunburstEffectsVHLComponent', () => {
  let component: SunburstEffectsVHLComponent;
  let fixture: ComponentFixture<SunburstEffectsVHLComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SunburstEffectsVHLComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SunburstEffectsVHLComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
